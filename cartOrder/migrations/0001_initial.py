# Generated by Django 4.0.1 on 2022-02-22 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homepage', '0003_alter_products_options_alter_products_desc'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(blank=True, max_length=100)),
                ('is_ordered', models.BooleanField(default=False)),
                ('total_cart_items', models.PositiveBigIntegerField(default=0)),
                ('total_price', models.FloatField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer+', to=settings.AUTH_USER_MODEL, verbose_name='customer')),
            ],
            options={
                'verbose_name_plural': 'shopping cart',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartItem_id', models.CharField(blank=True, max_length=100)),
                ('prod_quantity', models.IntegerField()),
                ('prod_price', models.FloatField(default=0)),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartOrder.cart')),
                ('prod_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.products')),
            ],
            options={
                'verbose_name_plural': 'shopping Cart Items',
            },
        ),
    ]