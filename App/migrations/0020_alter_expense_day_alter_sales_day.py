# Generated by Django 4.2.3 on 2023-09-05 07:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0019_alter_expense_day_alter_sales_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='day',
            field=models.CharField(default=datetime.datetime(2023, 9, 5, 7, 43, 55, 116150, tzinfo=datetime.timezone.utc), max_length=100),
        ),
        migrations.AlterField(
            model_name='sales',
            name='day',
            field=models.CharField(default=datetime.datetime(2023, 9, 5, 7, 43, 55, 116150, tzinfo=datetime.timezone.utc), max_length=80),
        ),
    ]
