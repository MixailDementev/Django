
from django.db import models



class Client(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    date_registration = models.DateField()

    def __str__(self):
        return f'Client_name: {self.name}, phone: {self.phone}, email: {self.email}'



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(default=999999.99, max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    date_add = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=2)
    image = models.ImageField(null=True)


    def __str__(self):
        return f'Product_name: {self.name}, price: {self.price}, quantity: {self.quantity}'



class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f'Customer: {self.customer}, products: {self.products}, total_price: {self.total_price}, date_ordered: {self.date_ordered}'






