from django.db import models
import uuid

# Create your models here.
class Item(models.Model):
    id = models.UUIDField(primary_key=True,default = uuid.uuid4)
    item_title = models.CharField(max_length=200)
    item_sku = models.CharField(max_length=200, unique= True)
    item_price = models.FloatField()
    item_purchase_price = models.FloatField()
    item_stock_quantity = models.IntegerField()
    item_hsn_code = models.CharField(max_length=200)
    item_tax_rate = models.IntegerField()
    item_images = models.TextField()
    item_desc = models.TextField()
    item_category = models.TextField()
    item_attributes = models.TextField()
    user_id = models.IntegerField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.item_sku

class Customer(models.Model):
    customer_id = models.UUIDField(primary_key=True,default = uuid.uuid4)
    name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    gst = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique= True)
    mobile = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=500)
    isActive = models.BooleanField(default=False)
    user_id = models.IntegerField()
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.email

class Vendor(models.Model):
    id = models.UUIDField(primary_key=True,default = uuid.uuid4)
    name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    gst = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique= True)
    mobile = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=500)
    isActive = models.BooleanField(default=False)
    user_id = models.IntegerField()
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.email

class Employee(models.Model):
    id = models.UUIDField(primary_key=True,default = uuid.uuid4)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique= True)
    mobile = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=500)
    isActive = models.BooleanField(default=False)
    user_id = models.IntegerField()
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.email

class PurchaseOrder(models.Model):
    id = models.UUIDField(primary_key=True,default = uuid.uuid4)
    po_number = models.CharField(max_length=200)
    total_product_amount = models.CharField(max_length=200)
    total_tax_amount = models.CharField(max_length=12)
    total_discount_amount = models.CharField(max_length=12)
    grand_total = models.CharField(max_length=12)
    user_id = models.IntegerField()
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.po_number

class PurchaseOrderItem(models.Model):
    id = models.UUIDField(primary_key=True,default = uuid.uuid4)
    po_number = models.CharField(max_length=255)
    item_sku = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    item_quantity = models.IntegerField()
    item_price = models.FloatField()
    item_tax_rate = models.FloatField()
    item_recieved_quantity = models.IntegerField()
    item_damage_quantity = models.IntegerField()
    item_return_quantity = models.IntegerField()
    isCompleted = models.BooleanField(default=False)
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.po_number + self.item_sku + str(self.item_quantity) + str(self.item_price)

class Order(models.Model):
    id = models.UUIDField(primary_key=True,default = uuid.uuid4)
    order_number = models.CharField(max_length=200)
    total_product_amount = models.CharField(max_length=200)
    total_tax_amount = models.CharField(max_length=12)
    total_discount_amount = models.CharField(max_length=12)
    grand_total = models.CharField(max_length=12)
    user_id = models.IntegerField()
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.order_number

class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True,default = uuid.uuid4)
    order_number = models.CharField(max_length=255)
    item_sku = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    item_quantity = models.IntegerField()
    item_price = models.FloatField()
    item_tax_rate = models.FloatField()
    item_recieved_quantity = models.IntegerField()
    item_damage_quantity = models.IntegerField()
    item_return_quantity = models.IntegerField()
    isCompleted = models.BooleanField(default=False)
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.order_number + self.item_sku + str(self.item_quantity) + str(self.item_price)

class Invoice(models.Model):
    id = models.UUIDField(primary_key=True,default = uuid.uuid4)
    invoice_number = models.CharField(max_length=200)
    total_product_amount = models.CharField(max_length=200)
    total_tax_amount = models.CharField(max_length=12)
    total_discount_amount = models.CharField(max_length=12)
    grand_total = models.CharField(max_length=12)
    user_id = models.IntegerField()
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.invoice_number

class InvoiceItem(models.Model):
    id = models.UUIDField(primary_key=True,default = uuid.uuid4)
    invoice_number = models.CharField(max_length=255)
    item_sku = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    item_quantity = models.IntegerField()
    item_price = models.FloatField()
    item_tax_rate = models.FloatField()
    item_recieved_quantity = models.IntegerField()
    item_damage_quantity = models.IntegerField()
    item_return_quantity = models.IntegerField()
    isCompleted = models.BooleanField(default=False)
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.invoice_number + self.item_sku + str(self.item_quantity) + str(self.item_price)
    