# Generated by Django 2.0 on 2018-02-11 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20180211_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='internalID',
            field=models.IntegerField(unique=True),
        ),
    ]