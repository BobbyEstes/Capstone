# Generated by Django 3.2.3 on 2021-06-26 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crate_sizing', '0017_order_total_width'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_height',
            field=models.IntegerField(default=0),
        ),
    ]
