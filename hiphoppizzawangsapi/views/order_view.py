from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from hiphoppizzawangsapi.models import User, Order

class OrderView(ViewSet):

    def retrieve(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Order.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        try:
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
        order.customer_name = request.data["customer_name"]
        order.customer_phone = request.data["customer_phone"]
        order.customer_email = request.data["customer_email"]
        order.order_type = request.data["order_type"]
        order.status = request.data["status"]
        order.payment_type = request.data["payment_type"]
        order.date_of_order_closure = request.data["date_of_order_closure"]
        order.tip_amount = request.data["tip_amount"]

        cashier = User.objects.get(uid=request.data["cashierId"])
        order.cashier = cashier
        order.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
          'cashier', 
          'customer_name', 
          'customer_phone', 
          'customer_email', 
          'order_type', 
          'status', 
          'payment_type', 
          'date_of_order_closure', 
          'tip_amount'
          )
        depth = 1
