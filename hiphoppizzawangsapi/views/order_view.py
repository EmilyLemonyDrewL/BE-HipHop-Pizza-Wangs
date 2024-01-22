from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from hiphoppizzawangsapi.models import User, Order, Item, OrderItem
from rest_framework.decorators import action

class OrderView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single orders

        Returns:
            Response -- JSON serialized order
        """
        order = Order.objects.get(pk=pk)
        
        orderitem_id = OrderItem.objects.filter(order=order.pk)
        items = []
        for item in orderitem_id:
            items.append(item.item_id)
        order.items = Item.objects.filter(pk__in=items)
        
        serializer = OrderSerializer(order, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        try:
            status_param = request.query_params.get('status')
            
            if status_param and status_param.lower() == 'closed':
                orders = Order.objects.filter(status='Closed')
            else:
                orders = Order.objects.all()

            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Order.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def create(self, request):
        cashier = User.objects.get(uid=request.data["cashierId"])

        order = Order.objects.create(
          cashier=cashier,
          customer_name = request.data["customer_name"],
          customer_phone = request.data["customer_phone"],
          customer_email = request.data["customer_email"],
          order_type = request.data["order_type"],
          status = request.data["status"],
          payment_type = request.data["payment_type"],
          date_of_order_closure = request.data["date_of_order_closure"],
          tip_amount = request.data["tip_amount"],
        )

        order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        
        order = Order.objects.get(pk=pk)
        
        cashier = User.objects.get(uid=request.data['cashierId'])
        
        order.customer_name = request.data["customer_name"]
        order.customer_phone = request.data["customer_phone"]
        order.customer_email = request.data["customer_email"]
        order.order_type = request.data["order_type"]
        order.status = request.data["status"]
        order.payment_type = request.data["payment_type"]
        order.date_of_order_closure = request.data["date_of_order_closure"]
        order.tip_amount = request.data["tip_amount"]

        order.save()
        
        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    # decorator for deleting an order item
    @action(methods=['delete'], detail=True)
    def delete_order_item(self, request, pk):
        # filter to grab order pk and item id via the join table
        try:
           order_item = request.data.get("order_item")
           OrderItem.objects.filter(order=pk, item=order_item).delete()
           return Response(None, status=status.HTTP_204_NO_CONTENT)
        except OrderItem.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    # decorator for adding an order item
    @action(methods=['post'], detail=True)
    def add_order_item(self, request, pk):
        
        item = Item.objects.get(pk=request.data["item"])
        order = Order.objects.get(pk=pk)
        order_item = OrderItem.objects.create(
            item=item,
            order=order
        )
        return Response({'message': 'Menu item added'}, status=status.HTTP_201_CREATED)
        
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'price', 'description')
        depth = 1

class OrderSerializer(serializers.ModelSerializer):
    
    items = ItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = (
          'id',
          'cashier', 
          'customer_name', 
          'customer_phone', 
          'customer_email', 
          'order_type', 
          'status', 
          'payment_type', 
          'date_of_order_closure', 
          'tip_amount',
          'items'
          )
        depth = 1
