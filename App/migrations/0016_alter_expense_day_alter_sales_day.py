# Generated by Django 4.2.3 on 2023-08-30 00:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0015_sales_pay_method_alter_expense_day_alter_sales_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='day',
            field=models.CharField(default=datetime.datetime(2023, 8, 30, 0, 9, 43, 968421, tzinfo=datetime.timezone.utc), max_length=100),
        ),
        migrations.AlterField(
            model_name='sales',
            name='day',
            field=models.CharField(default=datetime.datetime(2023, 8, 30, 0, 9, 43, 970416, tzinfo=datetime.timezone.utc), max_length=80),
        ),
    ]