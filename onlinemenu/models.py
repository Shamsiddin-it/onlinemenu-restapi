from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    CATEGORY = (
        ('breakfast', 'breakfast'),
        ('dinner', 'dinner'),
        ('supper', 'supper'),
        ('dessert', 'dessert'),
        ('drinks', 'drinks'),
        ('snacks', 'snacks'),
    )
    category = models.CharField(choices=CATEGORY, max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    preparetion_time = models.CharField(max_length=50)
    image = models.ImageField(upload_to='files/images', height_field=None, width_field=None, max_length=None)
    creaetd_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    

class Table(models.Model):
    type = models.CharField(max_length=50, default='table')
    number = models.IntegerField()
    max_people = models.IntegerField()
    STATUS = (
        ('full', 'full'),
        ('free', 'free'),
    )
    status = models.CharField(choices=STATUS, max_length=50, default='free')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.type} number {self.number}"

class Bill(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    customer = models.CharField(max_length=150)
    total_price = models.DecimalField( max_digits=8, decimal_places=2, default=0)
    created_at = models.DateTimeField( auto_now=True)
    is_paid = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    def save(self, *args, **kwargs):
        if self.is_paid:
            self.table.status = "free"
        else:
            self.table.status = "full"
        self.table.save()  
        super().save(*args, **kwargs)
    def __str__(self):
        return self.customer
    

class Order(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def save(self, *args, **kwargs):
        bill = self.bill
        total = bill.total_price + (self.dish.price*self.quantity)
        bill.total_price = total
        bill.save()
        super().save(*args, **kwargs)
    
