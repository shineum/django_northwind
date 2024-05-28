from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Territories)
class TerritoriesAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Employees)
class EmployeesAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Shippers)
class ShippersAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CustomerDemographics)
class CustomerDemographicsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Customers)
class CustomersAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Categories)
class CategoriesAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Suppliers)
class SuppliersAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Products)
class ProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Orders)
class OrdersAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OrderDetails)
class OrderDetailsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.USStates)
class USStatesAdmin(admin.ModelAdmin):
    pass
