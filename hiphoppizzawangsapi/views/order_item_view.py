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
        items = OrderItem.objects.all()
        serializer = OrderItemSerializer(items, many=True)
        response_data = serializer.data
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        order_id = request.data["orderId"]
        item_id = request.data["itemId"]

        order_item = OrderItem.objects.create(
            order_id=order_id,
            item_id=item_id,
            quantity=request.data["quantity"]
        )

        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data)

    def destroy(self, request, pk):
        order_item = OrderItem.objects.get(pk=pk)
        order_item.delete()
        return Response('Order item deleted', status=status.HTTP_204_NO_CONTENT)


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'item', 'quantity')
