# Generated by Django 4.1.7 on 2023-10-11 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingreso_egreso', '0007_alter_detalle_venta_precio_venta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_venta',
            name='precio_venta',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Precio de venta'),
        ),
    ]
