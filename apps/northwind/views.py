from django.shortcuts import render
from rest_framework import permissions, viewsets
from . import models
from . import serializers

# Create your views here.

class RegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Region to be viewed or edited.
    """
    queryset = models.Region.objects.all().order_by('region_id')
    serializer_class = serializers.RegionSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoriesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Categories to be viewed or edited.
    """
    queryset = models.Categories.objects.all().order_by('-category_id')
    serializer_class = serializers.CategoriesSerializer
    permission_classes = [permissions.IsAuthenticated]


class TerritoriesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Territories to be viewed or edited.
    """
    queryset = models.Territories.objects.all().order_by('territory_id')
    serializer_class = serializers.TerritoriesSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployeesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Employees to be viewed or edited.
    """
    queryset = models.Employees.objects.all().order_by('employee_id')
    serializer_class = serializers.EmployeesSerializer
    permission_classes = [permissions.IsAuthenticated]


class ShippersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Shippers to be viewed or edited.
    """
    queryset = models.Shippers.objects.all().order_by('shipper_id')
    serializer_class = serializers.ShippersSerializer
    permission_classes = [permissions.IsAuthenticated]


class CustomersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Customers to be viewed or edited.
    """
    queryset = models.Customers.objects.all().order_by('customer_id')
    serializer_class = serializers.CustomersSerializer
    permission_classes = [permissions.IsAuthenticated]


class SuppliersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Suppliers to be viewed or edited.
    """
    queryset = models.Suppliers.objects.all().order_by('supplier_id')
    serializer_class = serializers.SuppliersSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Products to be viewed or edited.
    """
    queryset = models.Products.objects.all().order_by('product_id')
    serializer_class = serializers.ProductsSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrdersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = models.Orders.objects.all().order_by('order_id')
    serializer_class = serializers.OrdersSerializer
    permission_classes = [permissions.IsAuthenticated]


class USStatesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows USStates to be viewed or edited.
    """
    queryset = models.USStates.objects.all().order_by('state_id')
    serializer_class = serializers.USStatesSerializer
    permission_classes = [permissions.IsAuthenticated]