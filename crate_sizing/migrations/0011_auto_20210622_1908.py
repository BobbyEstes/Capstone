# Generated by Django 3.2.3 on 2021-06-23 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crate_sizing', '0010_auto_20210618_1925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='job_numbs',
            new_name='height_list',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_num',
        ),
        migrations.AddField(
            model_name='order',
            name='job_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='sqft_list',
            field=models.IntegerField(default=0),
        ),
    ]
