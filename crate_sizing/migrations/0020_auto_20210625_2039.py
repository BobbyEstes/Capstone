# Generated by Django 3.2.3 on 2021-06-26 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crate_sizing', '0019_auto_20210625_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='height_list',
        ),
        migrations.RemoveField(
            model_name='order',
            name='sqft_list',
        ),
    ]
