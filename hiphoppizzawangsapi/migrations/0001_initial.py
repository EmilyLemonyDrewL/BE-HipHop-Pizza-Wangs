# Generated by Django 4.1.3 on 2024-01-10 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_phone', models.IntegerField()),
                ('customer_email', models.EmailField(max_length=50)),
                ('order_type', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=6)),
                ('payment_type', models.CharField(max_length=50)),
                ('date_of_order_closure', models.DateField()),
                ('tip_amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
                ('name', models.CharField(default='Cashier', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hiphoppizzawangsapi.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hiphoppizzawangsapi.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hiphoppizzawangsapi.user'),
        ),
    ]
