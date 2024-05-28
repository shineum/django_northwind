from rest_framework import serializers
from . import models


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Region
        exclude = []
        extra_kwargs = {
            'territories': {'lookup_field': 'region_id'}
        }
    territories = serializers.HyperlinkedRelatedField(
        view_name='territories-detail', 
        lookup_field="region_id", 
        many=True, 
        read_only=True
    )


class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Categories
        exclude = []


class TerritoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Territories
        exclude = []


class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Employees
        exclude = []


class ShippersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Shippers
        exclude = []


class CustomersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Customers
        exclude = []


class SuppliersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Suppliers
        exclude = []


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Products
        exclude = []


class OrdersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Orders
        exclude = []


class USStatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.USStates
        exclude = []
