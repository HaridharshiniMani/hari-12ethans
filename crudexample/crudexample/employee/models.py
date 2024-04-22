from django.db import models

# Create your models here.
 
class Employee(models.Model):  
    ISIN = models.IntegerField()  
    symbol = models.CharField(max_length=100)  
    date = models.IntegerField()  
    assetclass = models.CharField(max_length=15)  
    quantity=models.IntegerField()
    marketprice=models.IntegerField()
    costprice=models.IntegerField()
    class Meta:  
        db_table = "employee"