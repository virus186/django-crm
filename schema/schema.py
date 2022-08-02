from graphene_django import DjangoObjectType
import graphene

from crm.models import Item, PurchaseOrder, PurchaseOrderItem, Invoice, InvoiceItem, Order, OrderItem, Employee, Customer, Vendor

from crm.schema import (
    ItemModel, PurchaseOrderModel, PurchaseOrderItemModel, InvoiceModel, InvoiceItemModel, OrderModel, OrderItemModel, EmployeeModel, CustomerModel, VendorModel,
    CreateItem, CreatePurchaseOrder, CreatePurchaseOrderItem, CreateInvoice, CreateInvoiceItem, CreateOrder, CreateOrderItem, CreateEmployee, CreateCustomer,
    CreateVendor
)

class Mutation(graphene.ObjectType):
    create_item = CreateItem.Field()
    create_purchase_order = CreatePurchaseOrder.Field()
    create_purchase_order_item = CreatePurchaseOrderItem.Field()
    create_invoice = CreateInvoice.Field()
    create_invoice_item = CreateInvoiceItem.Field()
    create_order = CreateOrder.Field()
    create_order_item = CreateOrderItem.Field()
    create_employee = CreateEmployee.Field()
    create_customer = CreateCustomer.Field()
    create_vendor = CreateVendor.Field()


class Query(graphene.ObjectType):
    customers = graphene.List(CustomerModel, id=graphene.Int())
    vendors = graphene.List(VendorModel, id=graphene.Int())
    employees = graphene.List(EmployeeModel, id=graphene.Int())
    purchase_order = graphene.List(PurchaseOrderModel, id=graphene.Int())
    get_items = graphene.List(ItemModel, id=graphene.Int())


    def resolve_customers(self, info, id):
        return Customer.objects.filter(user_id= id)
    
    def resolve_vendors(self, info, id):
        return Vendor.objects.filter(user_id= id)
    
    def resolve_employees(self, info, id):
        return Employee.objects.filter(user_id= id)

    def resolve_purchase_order(self, info, id):
        return PurchaseOrder.objects.filter(id= id)

    def resolve_get_items(self, info, id):
        return Item.objects.filter(user_id= id)



schema = graphene.Schema(query=Query, mutation=Mutation)