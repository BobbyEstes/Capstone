# Generated by Django 3.2.3 on 2021-06-26 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crate_sizing', '0016_alter_job_numbers_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_width',
            field=models.IntegerField(default=0),
        ),
    ]
