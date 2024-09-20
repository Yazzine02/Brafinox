from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator


# Create your models here.
# -----------------------------------------------------------
class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    stock_unit = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    numero_bl = models.CharField(max_length=30)

    def __str__(self):
        return self.name

# -----------------------------------------------------------

class Client(models.Model):
    CLIENT_TYPE_CHOICES = [
        ('particulier','Particulier'),
        ('entreprise','Entreprise'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    client_type = models.CharField(
        max_length=20,
        choices=CLIENT_TYPE_CHOICES,
        default='particulier'
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.client_type})"
    
# -----------------------------------------------------------

class Sell(models.Model):
    STATUS_CHOICES = [
        ('pending','Pending'),
        ('completed','Completed')
    ]

    client= models.ForeignKey('Client', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    sell_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], editable=False)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    status = models.CharField(
        max_length=10,
        choices = STATUS_CHOICES,
        default='pending',
        editable=False
    )
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Sale to {self.client}ID of {self.product}ID * {self.quantity} on {self.date} with a status of: {self.status}"
    
    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.sell_price
        self.balance = self.total_price - self.amount_paid
        if self.amount_paid >= self.total_price:
            self.status = 'completed'
        else:
            self.status = 'pending'
        # Call the parent class's save method to save the object in the database
        super(Sell, self).save(*args, **kwargs)

# -----------------------------------------------------------

class Buy(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10,decimal_places=2, validators=[MinValueValidator(0)])
    total_price = models.DecimalField(max_digits=10,decimal_places=2, validators=[MinValueValidator(0)], editable= False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Purchase of product id {self.product}ID in a quantity of {self.quantity} with a total price of {self.total_price}DH"
    
    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.purchase_price
        super(Buy, self).save(*args, **kwargs)

# -----------------------------------------------------------

class Payment(models.Model):
    sell = models.ForeignKey('Sell',on_delete=models.CASCADE)
    client = models.ForeignKey('Client',on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2, validators=[MinValueValidator(0)])
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"Payment of {self.amount}DH for {self.sell}ID on {self.date} by {self.client}ID"