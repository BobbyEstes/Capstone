
from django.shortcuts import render
import mysql.connector
import math
from decouple import config
from .models import Cust_info, Order, Job_numbers

mydb = mysql.connector.connect(
    host=config("HOST"),
    user=config("USER"),
    password=config("PASSWORD"),
    database=config("DATABASE")
)

mycursor = mydb.cursor()


def shipping(request):
    return render(request, 'pages/shipping.html')


def get_cutlist(request):
    customer = request.POST.get("Customer")
    del_date = request.POST.get("del_date")

    mycursor.execute(f"""
    select
        so_detail.wo_id,
        max(so_detail.height) as max_height,
        sum(so_detail.selling_units) total_sf,
        cust_customers.custno,
        cust_customers.company,
        so_jobs.del_date,
        so_jobs.id as sono,
        so_jobs.pono,
        so_jobs.shipto_id,
        cust_shipaddress.address1,
        cust_shipaddress.address2,
        cust_shipaddress.city,
        cust_shipaddress.state,
        cust_shipaddress.zip,
        cust_shipaddress.plusfour,
        cust_shipaddress.county,
        cust_shipaddress.prefVia,
        cust_shipaddress.prefType,
        cust_delvia.name as delvia,
        cust_deltype.deltype as deltype
        from
        back_office.so_jobs
        join
        back_office.so_detail on so_jobs.id = so_detail.sono
        join
        back_office.cust_shipaddress on so_jobs.shipto_id = cust_shipaddress.id
        join
        back_office.cust_deltype on cust_shipaddress.prefType = cust_deltype.id
        join
        back_office.cust_delvia on cust_shipaddress.prefVia = cust_delvia.id
        join
        back_office.cust_customers on so_jobs.custno = cust_customers.custno
    where
        so_jobs.custno = '{customer}'
    and so_jobs.sostatus = 'scheduled'
    and so_jobs.del_date <= '{del_date}'
    group by so_detail.wo_id;""")

    myresult = mycursor.fetchall()

    customer = Cust_info.objects.create(cust_name=myresult[0][4], cust_no=myresult[0][3], street=myresult[0]
                                        [9], city=myresult[0][11], state=myresult[0][12], zip=myresult[0][13], ship_via=myresult[0][-1],)

    inside_crate_length = (myresult[0][1])
    sqft = (myresult[0][2])

    total_width = 39
    crate_length = (inside_crate_length + 1)
    crate_width = (total_width + 0)
    crate_height = (((inside_crate_length * crate_width)/144) + 2)
    crate_top_length = (inside_crate_length + .875)
    crate_top_width = (crate_width + .875)
    crate_bottom_length = inside_crate_length
    crate_bottom_width = (crate_width + 0)
    crate_sides_length = (inside_crate_length + .875)
    crate_sides_width = (crate_height + .5)
    crate_ends_length = (crate_width + .875)
    crate_ends_width = (crate_height + .5)
    corner_brace_length = (crate_height + 1)
    corner_brace_width = 3

    order = Order.objects.create(max_height=inside_crate_length, sqft=sqft, crate_height=crate_height, crate_width=crate_width, 
                                 corner_brace_width=corner_brace_width, corner_brace_length=corner_brace_length,
                                 crate_ends_width=crate_ends_width, crate_ends_length=crate_ends_length,
                                 crate_sides_width=crate_sides_width, crate_sides_length=crate_sides_length,
                                     crate_bottom_width=crate_bottom_width, crate_bottom_length=crate_bottom_length,
                                     crate_top_width=crate_top_width, crate_top_length=crate_top_length, crate_length=crate_length,
                                     customer=customer)
    
    
    for x in range(len(myresult)):
        print('job#', myresult[x][0])
        print('height', myresult[x][1])
        print('sqft', myresult[x][2])
        Job_numbers.objects.create(job_number=myresult[x][0], order=order)
        # Order.objects.create(max_height=myresult[x][1], sqft=myresult[x][2], customer=customer)
        # Order.objects.create(sqft=myresult[x][2], customer=customer)

        
    
    # customer = Cust_info.objects.all().filter(cust_no__exact="CON012").first() # querries the customer info looking for customer # and returns the first result
    # customer_id = Cust_info.objects.all().filter(cust_no__exact="CON012").first().id # returns the id associated with this customer
    # customer_order = Order.objects.all().filter(customer=customer_id) # filters by the foriegn key finding the order associated with this customer
    # customer_order_id = Order.objects.all().filter(customer=customer_id).first().id # filters by the foriegn key finding the id of the customer order
    # Job_number = Job_numbers.objects.all().filter(order=customer_order_id) # returns all job numbers associated with a spacific order
    # print(Job_number)
    orders = Order.objects.all()
    cust_info = Cust_info.objects.all()
    context = {
        'orders': orders,
        'cust_info': cust_info,
        # 'job_number': Job_number,
        # 'customer_order': customer_order
    }

    return render(request, 'pages/cut_list.html', context)
