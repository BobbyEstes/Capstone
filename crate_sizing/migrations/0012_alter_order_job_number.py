# Generated by Django 3.2.3 on 2021-06-24 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crate_sizing', '0011_auto_20210622_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='job_number',
            field=models.CharField(max_length=200),
        ),
    ]
