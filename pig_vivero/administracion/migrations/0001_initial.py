# Generated by Django 4.2.4 on 2023-11-18 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_total', models.FloatField(verbose_name='Monto total')),
                ('compra_abierta', models.BooleanField(default=True, verbose_name='Compra abierta')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=250, verbose_name='Descripcion')),
                ('precio', models.FloatField(verbose_name='Precio')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen del producto')),
                ('promocion', models.BooleanField(null=True, verbose_name='Promocion')),
                ('categoria', models.ManyToManyField(to='administracion.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCarrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='cantidad')),
                ('subtotal', models.FloatField(verbose_name='Subtotal')),
                ('carrito', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='administracion.carrito')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_de_cliente', models.IntegerField(verbose_name='Numero de cliente')),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=250, verbose_name='Apellido')),
                ('dni', models.IntegerField(verbose_name='DNI')),
                ('email', models.EmailField(max_length=250, verbose_name='E-Mail')),
                ('usuario', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='carrito',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.cliente'),
        ),
    ]
