# Generated by Django 4.1.3 on 2024-01-17 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hiphoppizzawangsapi', '0005_alter_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='hiphoppizzawangsapi.item'),
        ),
    ]
