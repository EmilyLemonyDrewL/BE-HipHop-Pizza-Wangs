# Generated by Django 4.2.7 on 2024-01-15 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiphoppizzawangsapi', '0004_rename_uid_order_cashier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]
