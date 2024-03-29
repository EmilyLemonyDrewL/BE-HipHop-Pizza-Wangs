from rest_framework.viewsets import ViewSet
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from hiphoppizzawangsapi.models import Revenue, Order
from django.db.models import Sum

class RevenueView(ViewSet):
  
    def retrieve(self, request, pk=None):
      try:
        total_revenue = Order.objects.filter(status='Closed').aggregate(total_revenue=Sum('tip_amount'))['total_revenue'] or 0
        
        revenue, created = Revenue.objects.get_or_create(pk=1)
        revenue.total_rev = total_revenue
        revenue.save()
        
        serializer = RevenueSerializer(revenue)
        return Response(serializer.data, status=status.HTTP_200_OK)
      except Exception as ex:
          return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
      model = Revenue
      fields = ('total_rev',)
