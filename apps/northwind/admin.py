from django.contrib import admin
from . import models

# Register your models here.

class _AdminReadOnlyTabularInline(admin.TabularInline):
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
        

class TerritoriesInline(_AdminReadOnlyTabularInline):
    model = models.Territories


class EmployeesInline(_AdminReadOnlyTabularInline):
    model = models.Employees    
    fields = ('employee_id', '__custom_name__', 'title')
    readonly_fields = ('__custom_name__', )

    def __custom_name__(self, obj):
        return obj.__str__()
    __custom_name__.short_description = "name"


class ProductsInline(_AdminReadOnlyTabularInline):
    model = models.Products
    fields = ('product_id', 'product_name', 'unit_price', 'units_on_order')


class OrdersInline(_AdminReadOnlyTabularInline):
    model = models.Orders
    fields = ('order_id', 'customer', 'order_date')


class OrderDetailsInline(_AdminReadOnlyTabularInline):
    model = models.OrderDetails
    fields = ('order_id', 'product_id', 'quantity')


@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ["region_id", "region_description"]
    inlines = [TerritoriesInline]


@admin.register(models.Territories)
class TerritoriesAdmin(admin.ModelAdmin):
    list_display = ["territory_id", "territory_description"]


@admin.register(models.Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ["employee_id", "__str__", "title", "reports_to"]
    inlines = [EmployeesInline, OrdersInline]


@admin.register(models.Shippers)
class ShippersAdmin(admin.ModelAdmin):
    list_display = ["company_name", "phone"]
    inlines = [OrdersInline]


@admin.register(models.Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ["customer_id", "company_name", "country", "contact_title", "contact_name"]
    inlines = [OrdersInline]


@admin.register(models.Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["category_id", "category_name", "description"]
    inlines = [ProductsInline]


@admin.register(models.Suppliers)
class SuppliersAdmin(admin.ModelAdmin):
    list_display = ["supplier_id", "company_name", "country", "contact_title", "contact_name"]
    inlines = [ProductsInline]


@admin.register(models.Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["product_id", "product_name", "supplier_id", "category_id", "units_in_stock", "discontinued"]
    inlines = [OrderDetailsInline]
    list_filter = ["supplier_id", "category_id"]
    search_fields = ["product_name", "supplier_id__company_name", "category_id__category_name"]


@admin.register(models.Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ["order_id", "customer", "employee", "order_date", "shipped_date", "ship_via", "ship_country"]
    inlines = [OrderDetailsInline]
    list_filter = ["customer", "employee", "order_date", "ship_via", "ship_country"]
    search_fields = ["order_id", "customer__customer_id", "customer__company_name", "ship_via__shipper_id", "ship_via__company_name"]


@admin.register(models.USStates)
class USStatesAdmin(admin.ModelAdmin):
    list_display = ["state_id", "state_name", "state_abbr", "state_region"]
