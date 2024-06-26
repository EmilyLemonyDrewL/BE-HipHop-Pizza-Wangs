"""hiphoppizzawangs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from rest_framework import routers
from hiphoppizzawangsapi.views import ItemView, OrderItemView, OrderView, RevenueView, check_user, register_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"orders", OrderView, 'order')
router.register(r"items", ItemView, 'item')
router.register(r"order_items", OrderItemView, 'order_item')
router.register(r"revenue", RevenueView, 'revenue')

def inspect_urls(request):
    print(router.urls)
    return HttpResponse("check console for URL patterns.")


urlpatterns = [
    path('inspect', inspect_urls),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('checkuser', check_user),
    path('register', register_user),
    path('api/order/total-revenue/', OrderView.as_view({'get': 'total_revenue'}), name='order-total-revenue'),
]
