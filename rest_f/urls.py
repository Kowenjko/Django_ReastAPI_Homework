from django.db import router
from django.urls import path,include
from rest_framework import routers
import rest_framework
from . import views

router = routers.DefaultRouter()
router.register(r'users-list',views.UsersViewSet)
router.register(r'address-list',views.AddressViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('address/',views.AddressView.AddressList.as_view()),
]