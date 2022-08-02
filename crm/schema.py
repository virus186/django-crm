from graphene_django import DjangoObjectType
import graphene

from .models import Item, PurchaseOrder, PurchaseOrderItem, Invoice, InvoiceItem, Order, OrderItem, Employee, Customer, Vendor
''' all models set '''
class ItemModel(DjangoObjectType):
    class Meta:
        model = Item

class PurchaseOrderModel(DjangoObjectType):
    class Meta:
        model = PurchaseOrder

class PurchaseOrderItemModel(DjangoObjectType):
    class Meta:
        model = PurchaseOrderItem

class InvoiceModel(DjangoObjectType):
    class Meta:
        model = Invoice

class InvoiceItemModel(DjangoObjectType):
    class Meta:
        model = InvoiceItem

class OrderModel(DjangoObjectType):
    class Meta:
        model = Order

class OrderItemModel(DjangoObjectType):
    class Meta:
        model = OrderItem

class EmployeeModel(DjangoObjectType):
    class Meta:
        model = Employee

class CustomerModel(DjangoObjectType):
    class Meta:
        model = Customer

class VendorModel(DjangoObjectType):
    class Meta:
        model = Vendor

''' all create mutation start '''

''' CreateItem mutation '''
class CreateItem(graphene.Mutation):
    item = graphene.Field(ItemModel)

    class Arguments:
        item_title =  graphene.String()
        item_sku =  graphene.String()
        item_price = graphene.Float()
        item_purchase_price = graphene.Float()
        item_stock_quantity = graphene.Int()
        item_hsn_code =  graphene.String()
        item_tax_rate = graphene.Int()
        item_images = graphene.String()
        item_desc = graphene.String()
        item_category = graphene.String()
        item_attributes = graphene.String()
        user_id = graphene.Int()

    def mutate(self, item_title, item_sku, item_price, item_purchase_price,item_stock_quantity,item_hsn_code,item_tax_rate,item_images,item_desc,item_category,item_attributes,user_id):
        d = Item(item_title = item_title,item_sku = item_sku,item_price = item_price,item_purchase_price = item_purchase_price,item_stock_quantity = item_stock_quantity,item_hsn_code = item_hsn_code,item_tax_rate = item_tax_rate,item_images = item_images,item_desc = item_desc,item_category = item_category,item_attributes = item_attributes,user_id = user_id)
        d.save()
        return CreateItem(item=d)

''' CreateVendor mutation '''
class CreateVendor(graphene.Mutation):
    vendor = graphene.Field(VendorModel)

    class Arguments:
        name = graphene.String()
        company_name = graphene.String()
        gst = graphene.String()
        email = graphene.String()
        mobile = graphene.String()
        password = graphene.String()
        isActive = graphene.Boolean()
        user_id = graphene.Int()
       

    def mutate(self, name, company_name, gst, email, mobile, password, isActive, user_id):
        d = Vendor(name = name, company_name = company_name, gst = gst, email = email, mobile = mobile, password = password, isActive = isActive, user_id = user_id)
        d.save()
        return CreateVendor(vendor=d)

''' CreateCustomer mutation '''
class CreateCustomer(graphene.Mutation):
    customer = graphene.Field(CustomerModel)

    class Arguments:
        name = graphene.String()
        company_name = graphene.String()
        gst = graphene.String()
        email = graphene.String()
        mobile = graphene.String()
        password = graphene.String()
        isActive = graphene.Boolean()
        user_id = graphene.Int()
       

    def mutate(self, name, company_name, gst, email, mobile, password, isActive, user_id):
        d = Customer(name = name, company_name = company_name, gst = gst, email = email, mobile = mobile, password = password, isActive = isActive, user_id = user_id)
        d.save()
        return CreateCustomer(customers=d)

''' CreateEmployee mutation '''
class CreateEmployee(graphene.Mutation):
    employee = graphene.Field(EmployeeModel)

    class Arguments:
        name = graphene.String()
        company_name = graphene.String()
        gst = graphene.String()
        email = graphene.String()
        mobile = graphene.String()
        password = graphene.String()
        isActive = graphene.Boolean()
        user_id = graphene.Int()
       

    def mutate(self, name, company_name, gst, email, mobile, password, isActive, user_id):
        d = Employee(name = name, company_name = company_name, gst = gst, email = email, mobile = mobile, password = password, isActive = isActive, user_id = user_id)
        d.save()
        return CreateEmployee(employee=d)


''' CreatePurchaseOrder mutation '''
class CreatePurchaseOrder(graphene.Mutation):
    purchaseOrder = graphene.Field(PurchaseOrderModel)

    class Arguments:
        po_number = graphene.String()
        total_product_amount = graphene.String()
        total_tax_amount = graphene.String()
        total_discount_amount = graphene.String()
        grand_total = graphene.String()
        user_id = graphene.Int()
       

    def mutate(po_number, total_product_amount, total_tax_amount, total_discount_amount, grand_total, user_id):
        d = PurchaseOrder(po_number = po_number, total_product_amount = total_product_amount, total_tax_amount = total_tax_amount, total_discount_amount = total_discount_amount, grand_total = grand_total, user_id = user_id)
        d.save()
        return CreatePurchaseOrder(purchaseOrder=d)


''' CreatePurchaseOrderItem mutation '''
class CreatePurchaseOrderItem(graphene.Mutation):
    purchaseOrderItem = graphene.Field(PurchaseOrderItemModel)

    class Arguments:
        po_number = graphene.String()
        item_sku = graphene.String()
        item_name = graphene.String()
        item_quantity = graphene.Int()
        item_price = graphene.Float()
        item_tax_rate = graphene.Float()
        item_recieved_quantity = graphene.Int()
        item_damage_quantity = graphene.Int()
        item_return_quantity = graphene.Int()
        isCompleted = graphene.Boolean()       

    def mutate(po_number, item_sku, item_name, item_quantity, item_price, item_tax_rate, item_recieved_quantity, item_damage_quantity, item_return_quantity, isCompleted):
        d = PurchaseOrderItem(po_number = po_number, item_sku = item_sku, item_name = item_name, item_quantity = item_quantity, item_price = item_price, item_tax_rate = item_tax_rate, item_recieved_quantity = item_recieved_quantity, item_damage_quantity = item_damage_quantity, item_return_quantity = item_return_quantity, isCompleted = isCompleted)
        d.save()
        return CreatePurchaseOrderItem(purchaseOrderItem=d)



''' CreateOrder mutation '''
class CreateOrder(graphene.Mutation):
    order = graphene.Field(OrderModel)

    class Arguments:
        order_number = graphene.String()
        total_product_amount = graphene.String()
        total_tax_amount = graphene.String()
        total_discount_amount = graphene.String()
        grand_total = graphene.String()
        user_id = graphene.Int()
       

    def mutate(order_number, total_product_amount, total_tax_amount, total_discount_amount, grand_total, user_id):
        d = Order(order_number = order_number, total_product_amount = total_product_amount, total_tax_amount = total_tax_amount, total_discount_amount = total_discount_amount, grand_total = grand_total, user_id = user_id)
        d.save()
        return CreateOrder(order=d)


''' CreateOrderItem mutation '''
class CreateOrderItem(graphene.Mutation):
    orderItem = graphene.Field(OrderItemModel)

    class Arguments:
        order_number = graphene.String()
        item_sku = graphene.String()
        item_name = graphene.String()
        item_quantity = graphene.Int()
        item_price = graphene.Float()
        item_tax_rate = graphene.Float()
        item_recieved_quantity = graphene.Int()
        item_damage_quantity = graphene.Int()
        item_return_quantity = graphene.Int()
        isCompleted = graphene.Boolean()       

    def mutate(order_number, item_sku, item_name, item_quantity, item_price, item_tax_rate, item_recieved_quantity, item_damage_quantity, item_return_quantity, isCompleted):
        d = OrderItem(order_number = order_number, item_sku = item_sku, item_name = item_name, item_quantity = item_quantity, item_price = item_price, item_tax_rate = item_tax_rate, item_recieved_quantity = item_recieved_quantity, item_damage_quantity = item_damage_quantity, item_return_quantity = item_return_quantity, isCompleted = isCompleted)
        d.save()
        return CreateOrderItem(orderItem=d)



''' CreateOrder mutation '''
class CreateInvoice(graphene.Mutation):
    invoice = graphene.Field(InvoiceModel)

    class Arguments:
        invoice_number = graphene.String()
        total_product_amount = graphene.String()
        total_tax_amount = graphene.String()
        total_discount_amount = graphene.String()
        grand_total = graphene.String()
        user_id = graphene.Int()
       

    def mutate(invoice_number, total_product_amount, total_tax_amount, total_discount_amount, grand_total, user_id):
        d = Invoice(invoice_number = invoice_number, total_product_amount = total_product_amount, total_tax_amount = total_tax_amount, total_discount_amount = total_discount_amount, grand_total = grand_total, user_id = user_id)
        d.save()
        return CreateInvoice(invoice=d)


''' CreateInvoiceItem mutation '''
class CreateInvoiceItem(graphene.Mutation):
    invoiceItem = graphene.Field(InvoiceItemModel)

    class Arguments:
        invoice_number = graphene.String()
        item_sku = graphene.String()
        item_name = graphene.String()
        item_quantity = graphene.Int()
        item_price = graphene.Float()
        item_tax_rate = graphene.Float()
        item_recieved_quantity = graphene.Int()
        item_damage_quantity = graphene.Int()
        item_return_quantity = graphene.Int()
        isCompleted = graphene.Boolean()       

    def mutate(invoice_number, item_sku, item_name, item_quantity, item_price, item_tax_rate, item_recieved_quantity, item_damage_quantity, item_return_quantity, isCompleted):
        d = InvoiceItem(invoice_number = invoice_number, item_sku = item_sku, item_name = item_name, item_quantity = item_quantity, item_price = item_price, item_tax_rate = item_tax_rate, item_recieved_quantity = item_recieved_quantity, item_damage_quantity = item_damage_quantity, item_return_quantity = item_return_quantity, isCompleted = isCompleted)
        d.save()
        return CreateInvoiceItem(invoiceItem=d)
