# Generated by Django 5.0.6 on 2024-05-27 15:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Category ID')),
                ('category_name', models.CharField(db_index=True, max_length=15, verbose_name='Category name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('picture', models.BinaryField(blank=True, null=True, verbose_name='Picture')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='CustomerDemographics',
            fields=[
                ('customer_type_id', models.CharField(max_length=5, primary_key=True, serialize=False, verbose_name='Customer typeID')),
                ('customer_desc', models.TextField(blank=True, null=True, verbose_name='Customer description')),
            ],
            options={
                'verbose_name': 'customerdemographic',
                'verbose_name_plural': 'customerdemographics',
                'db_table': 'customer_demographics',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region_id', models.PositiveSmallIntegerField(primary_key=True, serialize=False, verbose_name='Region id')),
                ('region_description', models.CharField(max_length=50, verbose_name='Region description')),
            ],
            options={
                'db_table': 'region',
            },
        ),
        migrations.CreateModel(
            name='Shippers',
            fields=[
                ('shipper_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Shipper ID')),
                ('company_name', models.CharField(max_length=40, verbose_name='Company name')),
                ('phone', models.CharField(blank=True, max_length=24, null=True, verbose_name='Phone')),
            ],
            options={
                'verbose_name': 'shipper',
                'verbose_name_plural': 'shippers',
                'db_table': 'shippers',
            },
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Supplier ID')),
                ('company_name', models.CharField(max_length=40, verbose_name='Company name')),
                ('contact_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Contact name')),
                ('contact_title', models.CharField(blank=True, max_length=30, null=True, verbose_name='Contact title')),
                ('address', models.CharField(blank=True, max_length=60, null=True, verbose_name='Address')),
                ('city', models.CharField(blank=True, max_length=15, null=True, verbose_name='City')),
                ('region', models.CharField(blank=True, max_length=15, null=True, verbose_name='Region')),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Postal code')),
                ('country', models.CharField(blank=True, max_length=15, null=True, verbose_name='Country')),
                ('phone', models.CharField(blank=True, max_length=24, null=True, verbose_name='Phone')),
                ('fax', models.CharField(blank=True, max_length=24, null=True, verbose_name='Fax')),
                ('homepage', models.TextField(blank=True, null=True, verbose_name='HomePage')),
            ],
            options={
                'verbose_name': 'supplier',
                'verbose_name_plural': 'suppliers',
                'db_table': 'suppliers',
            },
        ),
        migrations.CreateModel(
            name='USStates',
            fields=[
                ('state_id', models.SmallIntegerField(primary_key=True, serialize=False, verbose_name='State id')),
                ('state_name', models.CharField(max_length=100, verbose_name='State Name')),
                ('state_abbr', models.CharField(max_length=2, verbose_name='State Abbreviation')),
                ('state_region', models.CharField(max_length=50, verbose_name='State Region')),
            ],
            options={
                'verbose_name': 'us_state',
                'verbose_name_plural': 'us_states',
                'db_table': 'us_states',
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_id', models.CharField(max_length=5, primary_key=True, serialize=False, verbose_name='Customer ID')),
                ('company_name', models.CharField(max_length=40, verbose_name='Company name')),
                ('contact_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Contact name')),
                ('contact_title', models.CharField(blank=True, max_length=30, null=True, verbose_name='Contact title')),
                ('address', models.CharField(blank=True, max_length=60, null=True, verbose_name='Address')),
                ('city', models.CharField(blank=True, max_length=15, null=True, verbose_name='City')),
                ('region', models.CharField(blank=True, max_length=15, null=True, verbose_name='Region')),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Postal code')),
                ('country', models.CharField(blank=True, max_length=15, null=True, verbose_name='Country')),
                ('phone', models.CharField(blank=True, max_length=24, null=True, verbose_name='Phone')),
                ('fax', models.CharField(blank=True, max_length=24, null=True, verbose_name='Fax')),
                ('customer_customer_demo', models.ManyToManyField(blank=True, db_table='customer_customer_demo', to='northwind.customerdemographics', verbose_name='Customer customer demo')),
            ],
            options={
                'verbose_name': 'customer',
                'verbose_name_plural': 'customers',
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Employee id')),
                ('last_name', models.CharField(db_index=True, max_length=20, verbose_name='Last name')),
                ('first_name', models.CharField(max_length=10, verbose_name='First name')),
                ('title', models.CharField(blank=True, max_length=30, null=True, verbose_name='title')),
                ('title_of_courtesy', models.CharField(blank=True, max_length=25, null=True, verbose_name='Title of Courtesy')),
                ('birth_date', models.DateTimeField(blank=True, null=True, verbose_name='Birth date')),
                ('hire_date', models.DateTimeField(blank=True, null=True, verbose_name='Hire date')),
                ('address', models.CharField(blank=True, max_length=60, null=True, verbose_name='address')),
                ('city', models.CharField(blank=True, max_length=15, null=True, verbose_name='City')),
                ('region', models.CharField(blank=True, max_length=15, null=True, verbose_name='Region')),
                ('postal_code', models.CharField(blank=True, db_index=True, max_length=10, verbose_name='Postal code')),
                ('country', models.CharField(blank=True, max_length=15, null=True, verbose_name='Country')),
                ('home_phone', models.CharField(blank=True, max_length=24, null=True, verbose_name='Home phone')),
                ('extension', models.CharField(blank=True, max_length=4, null=True, verbose_name='Extension')),
                ('photo', models.BinaryField(blank=True, null=True, verbose_name='Photo')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
                ('photo_path', models.CharField(blank=True, max_length=255, null=True, verbose_name='Photo path')),
                ('reports_to', models.ForeignKey(blank=True, db_column='reports_to', null=True, on_delete=django.db.models.deletion.PROTECT, to='northwind.employees')),
            ],
            options={
                'verbose_name': 'employee',
                'verbose_name_plural': 'employees',
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Order ID')),
                ('order_date', models.DateField(blank=True, db_index=True, null=True, verbose_name='Order date')),
                ('required_date', models.DateField(blank=True, null=True, verbose_name='Required_date')),
                ('shipped_date', models.DateField(blank=True, db_index=True, null=True, verbose_name='Shipped date')),
                ('freight', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='Freight')),
                ('ship_name', models.CharField(blank=True, max_length=40, null=True, verbose_name='Ship name')),
                ('ship_address', models.CharField(blank=True, max_length=60, null=True, verbose_name='Ship address')),
                ('ship_city', models.CharField(blank=True, max_length=15, null=True, verbose_name='Ship city')),
                ('ship_region', models.CharField(blank=True, max_length=15, null=True, verbose_name='Ship region')),
                ('ship_postal_code', models.CharField(blank=True, db_index=True, max_length=10, null=True, verbose_name='Ship postal code')),
                ('ship_country', models.CharField(blank=True, max_length=15, null=True, verbose_name='Shipped country')),
                ('customer', models.ForeignKey(blank=True, db_column='customer_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='northwind.customers')),
                ('employee', models.ForeignKey(blank=True, db_column='employee_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='northwind.employees')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=4, max_digits=19, verbose_name='Unit price')),
                ('quantity', models.SmallIntegerField(verbose_name='Quantity')),
                ('discount', models.FloatField(verbose_name='Discount')),
                ('order_id', models.ForeignKey(db_column='order_id', on_delete=django.db.models.deletion.CASCADE, to='northwind.orders')),
            ],
            options={
                'verbose_name': 'order_detail',
                'verbose_name_plural': 'order_details',
                'db_table': 'order_details',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Product ID')),
                ('product_name', models.CharField(db_index=True, max_length=40, verbose_name='Product name')),
                ('quantity_per_unit', models.CharField(blank=True, max_length=20, null=True, verbose_name='Quantity per Unit')),
                ('unit_price', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='Unit price')),
                ('units_in_stock', models.SmallIntegerField(blank=True, null=True, verbose_name='Units in Stock')),
                ('units_on_order', models.SmallIntegerField(blank=True, null=True, verbose_name='Units on Order')),
                ('reorder_level', models.SmallIntegerField(blank=True, null=True, verbose_name='Reorder level')),
                ('discontinued', models.IntegerField(verbose_name='Discontinued')),
                ('category_id', models.ForeignKey(blank=True, db_column='category_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='northwind.categories')),
                ('supplier_id', models.ForeignKey(blank=True, db_column='supplier_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='northwind.suppliers')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'products',
            },
        ),
        migrations.AddField(
            model_name='orders',
            name='order_details',
            field=models.ManyToManyField(blank=True, through='northwind.OrderDetails', to='northwind.products', verbose_name='Products'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='product_id',
            field=models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, to='northwind.products'),
        ),
        migrations.AddField(
            model_name='orders',
            name='ship_via',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='northwind.shippers'),
        ),
        migrations.CreateModel(
            name='Territories',
            fields=[
                ('territory_id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Territory id')),
                ('territory_description', models.CharField(max_length=50, verbose_name='Territory description')),
                ('region_id', models.ForeignKey(db_column='region_id', on_delete=django.db.models.deletion.CASCADE, to='northwind.region')),
            ],
            options={
                'verbose_name': 'territory',
                'verbose_name_plural': 'territories',
                'db_table': 'territories',
            },
        ),
        migrations.AddField(
            model_name='employees',
            name='territories',
            field=models.ManyToManyField(blank=True, db_table='employee_territories', to='northwind.territories', verbose_name='Territories'),
        ),
    ]
