from django.db import models

class Product(models.Model):
    productID = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=100)
    productDescription = models.TextField()
    productPrice = models.DecimalField(max_digits=10, decimal_places=2)
    productStock = models.IntegerField()

    def __str__(self):
        return self.productName
    
class Customer(models.Model):
    customerId = models.AutoField(primary_key=True)
    customerName = models.CharField(max_length=200)
    customerEmail = models.EmailField(unique=True)
    customerPhone = models.CharField(max_length=15)

    def __str__(self):
        return self.customerName
    
class status(models.Model):
    id = models.CharField(max_length=1, primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    customerId = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.ForeignKey(status, on_delete=models.CASCADE)
    transactionDate = models.DateTimeField()
    createdBy = models.CharField(max_length=100)
    createdOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.productId.productName} for {self.customerId.customerName}"