from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'region', views.RegionViewSet)
router.register(r'categories', views.CategoriesViewSet)
router.register(r'territories', views.TerritoriesViewSet)
router.register(r'employees', views.EmployeesViewSet)
router.register(r'shippers', views.ShippersViewSet)
router.register(r'customers', views.CustomersViewSet)
router.register(r'suppliers', views.SuppliersViewSet)
router.register(r'products', views.ProductsViewSet)
router.register(r'orders', views.OrdersViewSet)
router.register(r'usstates', views.USStatesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
