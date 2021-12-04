from django.db import models
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _





class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE,verbose_name=_("Username"))
    name = models.CharField(max_length=20, null=True,verbose_name=_("Full Name"))
    email = models.EmailField(verbose_name=_("Email"))
    phone = models.CharField(max_length=11, blank=True, null=True,verbose_name=_("Mobile"))


    def __str__(self):
        return str(self.name)

@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
    instance.customer.save()




class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name=_("Name"))
    CATslug = models.SlugField(blank=True, null=True , verbose_name="slug")



    def save(self , *args  ,**kwargs ):
        self.CATsLug = slugify(self.name)
        super(Category , self).save( *args , **kwargs)
    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField(max_length=56, verbose_name=_("Product Name"),unique=True)
    name_ar = models.CharField(max_length=56, verbose_name=_("Product Name"))
    image = models.ImageField(upload_to='prodcut_img/' , verbose_name=_("Change Image"))
    price = models.DecimalField(max_digits=7  , decimal_places=1 , verbose_name=_("Price"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("category"))
    digital = models.BooleanField(default=False,null=True, blank=True)
    like = models.ManyToManyField(Customer,blank=True, verbose_name=_("Like"))
    discription = models.TextField(max_length=200, blank=True, null=True, verbose_name=_("Description"))
    discription_ar = models.TextField(max_length=200, blank=True, null=True, verbose_name=_("Description"))
    PRDSLug = models.SlugField(blank=True, null=True , verbose_name="slug")



    def save(self , *args  ,**kwargs ):
        self.PRDSLug = slugify(self.name)
        super(Product , self).save( *args , **kwargs)

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.PRDSLug})

    @property
    def likeNumber(self):
    	return self.like.all().count()


    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True



    def __str__(self):
        return self.name



class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE, verbose_name=_("Customer"))
    date_ordered = models.DateTimeField(auto_now_add=True, verbose_name=_("Order Date"))
    complete = models.BooleanField(default=False, verbose_name=_("Complete"))
    transaction_id = models.CharField(max_length=100, null=True, verbose_name=_("Transaction Id"))
    class Meta:
        ordering = ['-complete',]


    @property
    def shipping(self):
    	shipping = False
    	orderitems = self.orderitem_set.all()
    	for i in orderitems:
    		if i.product.digital == False:
    			shipping = True
    	return shipping



    @property
    def get_cart_total(self):
	    orderitems = self.orderitem_set.all()
	    total = sum([item.get_total for item in orderitems])
	    return total 

    @property
    def get_cart_items(self):
    	orderitems = self.orderitem_set.all()
    	total = sum([item.quantity for item in orderitems])
    	return total 

    def __str__(self):
	    return "Order details " +str(self.customer)



class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
    	total = self.product.price * self.quantity
    	return total
        
    def __str__(self):
	    return str(self.product)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return self.address