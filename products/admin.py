from django.contrib import admin
from .models import Customer, Product, Order, OrderItem, ShippingAddress, Category


admin.site.register(Category)

class CustomerAdmin(admin.ModelAdmin):
    fields = ('user','name','email','phone')
    readonly_fields = ('user','name','email','phone')



admin.site.register(Customer, CustomerAdmin)


class orderLineItem(admin.TabularInline):
    model = OrderItem
    readonly_fields = ['product','quantity',]
    extra = 0

class addressLineItem(admin.TabularInline):
    model = ShippingAddress
    fields = ('address','city','zipcode')
    readonly_fields = ['address','city','zipcode']
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ('admin_photo','name','category')
    fields = ('name','name_ar','category','admin_photo','image','price','discription','discription_ar','digital',)
    readonly_fields = ('admin_photo','PRDSLug',)
    list_display_links=('admin_photo','name',)
    search_fields = ['name','name_ar']
    list_filter = ('category',)

    

    # inlines = [orderLineItem]
admin.site.register(Product, ProductAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order','product','quantity',)




class OrderAdmin(admin.ModelAdmin):
    # def fk_phone(self, obj):
    #     return obj.customer.phone
    fields = (('customer' ,'complete',),'transaction_id')

    list_display = ('customer','complete','date_ordered',)
    readonly_fields = ['customer','complete','transaction_id']
    list_filter = ('complete',)
    inlines = [orderLineItem,addressLineItem]





class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('address','city','state','zipcode')



admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderItem, OrderItemAdmin)
# admin.site.register(ShippingAddress, ShippingAddressAdmin)