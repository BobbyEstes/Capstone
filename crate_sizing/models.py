from django.db import models
from django.db.models.base import Model


class Cust_info(models.Model):
    cust_name = models.CharField(max_length=200)
    cust_no = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    ship_via = models.CharField(max_length=200)

    def __str__(self):
        return "%s %s %s %s %s %s %s" % (self.cust_name, self.cust_no, self.street, self.city, self.state, self.zip, self.ship_via,)


class Order(models.Model):
    customer = models.ForeignKey(
        Cust_info, on_delete=models.PROTECT, blank=False)
    height_list = models.IntegerField(default=0)
    sqft_list = models.IntegerField(default=0)
    crate_length = models.IntegerField(default=0)
    crate_width = models.IntegerField(default=0)
    crate_height = models.IntegerField(default=0)
    crate_top_length = models.IntegerField(default=0)
    crate_top_width = models.IntegerField(default=0)
    crate_bottom_length = models.IntegerField(default=0)
    crate_bottom_width = models.IntegerField(default=0)
    crate_sides_length = models.IntegerField(default=0)
    crate_sides_width = models.IntegerField(default=0)
    crate_ends_length = models.IntegerField(default=0)
    crate_ends_width = models.IntegerField(default=0)
    corner_brace_length = models.IntegerField(default=0)
    corner_brace_width = models.IntegerField(default=0)
    sq_ft = models.IntegerField(default=0)
    
    def __str__(self):
        return "%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d" % (self.height_list, self.sqft_list, self.crate_length, self.crate_width, self.crate_height, self.crate_top_length, self.crate_top_width, self.crate_bottom_length, self.crate_bottom_width, self.crate_sides_length, self.crate_sides_width, self.crate_ends_length, self.crate_ends_width, self.corner_brace_length, self.corner_brace_width,)


class Job_numbers(models.Model):
    job_number = models.CharField(max_length=200)
    order = models.ForeignKey(Order, on_delete=models.PROTECT, blank=False, null=True)

    
    def __str__(self):
        return "%s %s" % (self.job_number, self.order,)