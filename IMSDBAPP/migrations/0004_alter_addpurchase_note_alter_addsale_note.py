# Generated by Django 4.2.1 on 2023-06-18 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMSDBAPP', '0003_addpurchase_sale_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addpurchase',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='addsale',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]