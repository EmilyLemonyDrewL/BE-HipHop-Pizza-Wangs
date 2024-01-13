from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from hiphoppizzawangsapi.models import Order, Item, OrderItem


class OrderItemView(ViewSet):

    def retrieve(self, request, pk):
        try:
            order_item = OrderItem.objects.get(pk=pk)
            serializer = OrderItemSerializer(order_item)
            return Response(serializer.data)
        except OrderItem.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        def list(self, request):
            order_items = OrderItem.objects.all()
            serializer = OrderItemSerializer(order_items, many=True)
            return Response(serializer.data)

    def create(self, request):
        order = request.data["order"]
        item = request.data["item"]

        try:
            order = Order.objects.get(id=order)
        except Order.DoesNotExist:
            return Response(
            {"error": "order does not exist"}, status=status.HTTP_404_NOT_FOUND
            )

        try:
            item = Item.objects.get(id=item)
        except Item.DoesNotExist:
            return Response(
              {"error": "item does not exist"}, status=status.HTTP_404_NOT_FOUND
            )

        order_item = OrderItem.objects.create(
            order = order,
            item = item,
            quantity = request.data["quantity"],
        )
        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        order_item = OrderItem.objects.get(pk=pk)
        order_item.quantity = request.data["quantity"]
        order_item.order = Order.objects.get(pk=request.data["order"])
        order_item.item = Item.objects.get(pk=request.data["item"])
        order_item.save()

        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        order_item = OrderItem.objects.get(pk=pk)
        order_item.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'item', 'quantity')
        depth = 1
