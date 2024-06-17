from django.db import models
# Create your models here.
class detail(models.Model):
    name = models.CharField(max_length=16)
    email = models.CharField(max_length=20)
    phone = models.IntegerField()
    username = models.CharField(max_length=30)
    passw = models.CharField(max_length=12)


class product(models.Model):
    productname = models.CharField(max_length=16)
    productprice = models.IntegerField()
    quantity = models.IntegerField()
    images=models.FileField()
    # category_name=models.CharField(max_length=300)
    # subcategory_name = models.CharField(max_length=100)

class booking(models.Model):
    user_details=models.ForeignKey(detail,on_delete=models.CASCADE)
    product_details=models.ForeignKey(product,on_delete=models.CASCADE)
    date=models.DateTimeField()
class PasswordReset(models.Model):
   user = models.ForeignKey(detail, on_delete=models.CASCADE)
   token=models.CharField(max_length=30)



class cart(models.Model):
    user_details=models.ForeignKey(detail,on_delete=models.CASCADE)
    product_details=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
class Order(models.Model):
    user = models.ForeignKey(detail, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    zip_code = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=15)
    notes = models.CharField(max_length=50)
    product_order = models.ForeignKey(product, on_delete=models.CASCADE)
    quantities = models.IntegerField(default=1)
    total_price = models.IntegerField()
    payment_status =models.CharField(max_length=20,null=True)
    purchase_date = models.DateTimeField(auto_now=True, null=True)
    product_status = models.CharField(max_length=50,null=True, default='Order Placed')
    instruction = models.CharField(max_length=50,null=True, default='Your Order Has Been Successfully Placed')

class Wishlist(models.Model):
    wishlist_product_details = models.ForeignKey(product,on_delete=models.CASCADE)
    wishlist_user_details = models.ForeignKey(detail,on_delete=models.CASCADE)
    wishlist_quantity = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f'{self.wishlist_user_details}'
