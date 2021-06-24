# Generated by Django 3.2.3 on 2021-06-09 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crate_sizing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cust_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=200)),
                ('cust_no', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.CharField(max_length=200)),
                ('ship_via', models.CharField(max_length=200)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crate_sizing.cust_info')),
            ],
        ),
        migrations.RemoveField(
            model_name='order_nums',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Header_info',
        ),
        migrations.DeleteModel(
            name='Order_nums',
        ),
    ]
