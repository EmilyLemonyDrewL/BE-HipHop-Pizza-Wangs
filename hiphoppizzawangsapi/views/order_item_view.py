from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from hiphoppizzawangsapi.models import Order, Item, OrderItem


class OrderItemView(ViewSet):

    def retrieve(self, request, pk):
        """GET single order item"""
        order_item = OrderItem.objects.get(pk=pk)
        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        """GET all order items"""
        order_items = OrderItem.objects.all()
        serializer = OrderItemSerializer(order_items, many=True)
        response_data = serializer.data
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        order = Order.objects.get(pk=request.data['order'])
        item = Item.objects.get(pk=request.data['item'])
        
        order_item = OrderItem.objects.create(
            order=order,
            item=item,
            quantity=request.data['quantity']
        )
        
        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        order_item = OrderItem.objects.get(pk=pk)
        order = Order.objects.get(pk=request.data['orderId'])
        item = Item.objects.get(pk=request.data['itemId'])
        
        order_item.order = order
        order_item.item = item
        order_item.quantity = request.data['quantity']
        
        order_item.save()
        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def destroy(self, request, pk):
        order_item = OrderItem.objects.get(pk=pk)
        order_item.delete()
        return Response('Order item deleted', status=status.HTTP_204_NO_CONTENT)


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'item', 'quantity')
