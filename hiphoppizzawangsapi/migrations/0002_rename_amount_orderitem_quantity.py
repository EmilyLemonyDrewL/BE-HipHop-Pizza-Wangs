# Generated by Django 4.1.3 on 2024-01-10 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hiphoppizzawangsapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='amount',
            new_name='quantity',
        ),
    ]
