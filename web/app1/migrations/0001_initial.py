# Generated by Django 3.0 on 2019-12-13 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=60)),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=60)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('familia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Familia')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=12)),
                ('fecha', models.CharField(max_length=60)),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=4)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='VentaLinea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=4)),
                ('iva', models.DecimalField(decimal_places=2, max_digits=4)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Venta')),
            ],
        ),
    ]
