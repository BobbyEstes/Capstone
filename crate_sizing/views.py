
from django.shortcuts import render
import mysql.connector
from decouple import config
from .models import Cust_info, Order


def shipping(request):
    return render(request, 'pages/shipping.html')


def get_cutlist(request):
    customer = request.POST.get("Customer")
    del_date = request.POST.get("del_date")

    mydb = mysql.connector.connect(
        host=config("HOST"),
        user=config("USER"),
        password=config("PASSWORD"),
        database=config("DATABASE")
    )

    mycursor = mydb.cursor()

    mycursor.execute(f"""
    select
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
        back_office.so_jobs join back_office.cust_shipaddress
        on so_jobs.shipto_id = cust_shipaddress.id join
        back_office.cust_deltype on cust_shipaddress.prefType = cust_deltype.id join
        back_office.cust_delvia on cust_shipaddress.prefVia = cust_delvia.id join
        back_office.cust_customers on so_jobs.custno = cust_customers.custno
    where
        so_jobs.custno = '{customer}'
    and so_jobs.sostatus = 'scheduled'
    and so_jobs.del_date <= '{del_date}';""")

    myresult = mycursor.fetchall()

    customer = Cust_info.objects.create(cust_name=myresult[0][1], cust_no=myresult[0][0], street=myresult[0]
                                        [6], city=myresult[0][8], state=myresult[0][9], zip=myresult[0][10], ship_via=myresult[0][-1],)

    for x in range(len(myresult)):
        Order.objects.create(order_num=myresult[x][3], customer=customer)
    context = {
        'customer': customer
    }

    return render(request, 'pages/cut_list.html', context)
