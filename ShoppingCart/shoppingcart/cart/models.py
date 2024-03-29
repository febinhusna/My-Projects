from django.db import models
from shoppingcart_app.models import Product

# Create your models here.
class Cart(models.Model):
    cart_id=models.CharField(max_length=250,blank=True)
    date=models.DateField(auto_now_add=True)
    img=models.ImageField(upload_to='Gallery')

    class Meta:
        db_table='cart'
        ordering=['date']

    def __str__(self):
        return '{}'.format(self.cart_id)

class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)
    img=models.ImageField(upload_to='Gallery')

    class Meta:
        db_table='cartItem'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return '{}'.format(self.product)
