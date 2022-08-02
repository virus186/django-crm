from django.contrib import admin

# Register your models here.

from .models import Item, PurchaseOrder, PurchaseOrderItem, Invoice, InvoiceItem, Order, OrderItem, Employee, Customer, Vendor

admin.site.register(Item)
admin.site.register(PurchaseOrder)
admin.site.register(PurchaseOrderItem)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Vendor)