from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.db.models import Sum

# Create your models here.
# -----------------------------------------------------------
class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    stock_unit = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    numero_bl = models.CharField(max_length=30,null=True, blank=True)

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
    PAYMENT_STATUS_CHOICES = [
        ('pending','Pending'),
        ('completed','Completed')
    ]
    PAYMENT_CHOICES = [
        ('carte bancaire','Carte Bancaire'),
        ('espece','Espece'),
    ]
    client= models.ForeignKey('Client', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    bl = models.ForeignKey('BL', to_field='bl_code', on_delete=models.CASCADE, related_name='sells')
    quantity = models.PositiveIntegerField()
    sell_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], editable=False)
    payment_mode = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES,
        default='espece',
    )
    status = models.CharField(
        max_length=10,
        choices = PAYMENT_STATUS_CHOICES,
        default='pending',
        editable=False
    )
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Sold to {self.client}ID of {self.product}ID * {self.quantity} on {self.date} with a status of: {self.status}"
    
    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.sell_price
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
    #change sell to bl
    bl = models.ForeignKey('BL', to_field='bl_code',on_delete=models.CASCADE)
    client = models.ForeignKey('Client',on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2, validators=[MinValueValidator(0)])
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"Payment of {self.amount}DH for {self.sell}ID on {self.date} by {self.client}ID"
    
# -----------------------------------------------------------

class BL(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending','Pending'),
        ('completed','Completed')
    ]
    bl_code = models.CharField(max_length=30, primary_key=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payment_status = models.CharField(max_length=15, choices=PAYMENT_STATUS_CHOICES, default='pending')
    bl_date = models.DateTimeField(default=timezone.now)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    balance = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    
    def __str__(self):
        return f"BL #{self.id} for {self.client.first_name} {self.client.last_name}"

    def update_payment_status(self):
        if self.amount_paid >= self.total_amount:
            self.payment_status = 'paid_in_full'
        else:
            self.payment_status = 'pending'
        self.save()

    def save(self, *args, **kwargs):
        self.balance = self.total_price - self.amount_paid
        super(BL, self).save(*args, **kwargs)

    @property
    def remaining_balance(self):
        return self.total_amount - self.amount_paid