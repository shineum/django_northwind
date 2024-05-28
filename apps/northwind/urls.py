from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
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

schema_view = get_schema_view(
    openapi.Info(
        title="Northwind API", 
        default_version='v1', 
    ),
    public=True,
)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),    
]
