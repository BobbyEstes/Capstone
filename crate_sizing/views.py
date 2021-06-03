
from django.shortcuts import render
import mysql.connector
from decouple import config


def shipping(request):
    

    mydb = mysql.connector.connect(
        host=config("HOST"),
        user=config("USER"),
        password=config("PASSWORD"),
        database=config("DATABASE")
    )

    mycursor = mydb.cursor()

    mycursor.execute("""
    select
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
        back_office.cust_delvia on cust_shipaddress.prefVia = cust_delvia.id
    where
        so_jobs.custno = 'THE004'
    and so_jobs.sostatus = 'scheduled'
    and so_jobs.del_date <= '2021-06-01';""")

    myresult = mycursor.fetchall()
    print(myresult)
    # my_string = ""
    for x in myresult:
        # my_string = + x
        print(x)
    return render(request, 'pages/shipping.html')
