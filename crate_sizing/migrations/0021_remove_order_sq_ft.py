# Generated by Django 3.2.3 on 2021-06-30 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crate_sizing', '0020_auto_20210625_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='sq_ft',
        ),
    ]