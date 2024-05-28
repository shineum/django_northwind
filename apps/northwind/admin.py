from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ["region_id", "region_description"]


@admin.register(models.Territories)
class TerritoriesAdmin(admin.ModelAdmin):
    list_display = ["territory_id", "territory_description"]


@admin.register(models.Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ["employee_id", "__str__", "title", "reports_to"]


@admin.register(models.Shippers)
class ShippersAdmin(admin.ModelAdmin):
    list_display = ["company_name", "phone"]


@admin.register(models.Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ["customer_id", "company_name", "country", "contact_title", "contact_name"]


@admin.register(models.Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["category_id", "category_name", "description"]


@admin.register(models.Suppliers)
class SuppliersAdmin(admin.ModelAdmin):
    list_display = ["supplier_id", "company_name", "country", "contact_title", "contact_name"]


@admin.register(models.Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["product_id", "product_name", "supplier_id", "category_id", "units_in_stock", "discontinued"]


@admin.register(models.Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ["order_id", "customer", "employee", "order_date", "shipped_date", "ship_via", "ship_country"]


@admin.register(models.USStates)
class USStatesAdmin(admin.ModelAdmin):
    list_display = ["state_id", "state_name", "state_abbr", "state_region"]
