# Generated by Django 4.2.5 on 2023-10-10 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('compras', '0002_initial'),
        ('ventas', '0001_initial'),
        ('producto', '0001_initial'),
        ('ingreso_egreso', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle_venta',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.venta', verbose_name='Venta'),
        ),
        migrations.AddField(
            model_name='detalle_compra',
            name='compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.compra', verbose_name='Compra'),
        ),
        migrations.AddField(
            model_name='detalle_compra',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.producto', verbose_name='Nombre'),
        ),
    ]
