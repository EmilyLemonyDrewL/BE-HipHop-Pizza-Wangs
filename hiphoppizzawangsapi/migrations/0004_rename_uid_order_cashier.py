# Generated by Django 4.1.3 on 2024-01-15 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hiphoppizzawangsapi', '0003_alter_orderitem_item_alter_orderitem_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='uid',
            new_name='cashier',
        ),
    ]