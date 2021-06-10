from django.db import models
from django.db.models.base import Model

# def header_info(request):
#     cust_name = (myresult[0][2])


class Cust_info(models.Model):
    cust_name = models.CharField(max_length=200)
    cust_no = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    ship_via = models.CharField(max_length=200)
    
    
    def __str__(self):
        return "%s %s %s %s %s"%(self.cust_name, self.street, self.city, self.state, self.ship_via,)

class Order(models.Model):
    customer = models.ForeignKey(Cust_info,on_delete=models.PROTECT,blank=False)
    order_num = models.CharField(max_length=200)
    
    
    
    def __str__(self):
        return "%s %s"%(self.customer, self.order_num)