# Generated by Django 2.0 on 2018-02-11 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20180211_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderCreationTime',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderID',
            field=models.CharField(max_length=120),
        ),
    ]
