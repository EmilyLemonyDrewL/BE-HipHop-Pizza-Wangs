# Generated by Django 4.1.3 on 2024-01-23 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiphoppizzawangsapi', '0006_alter_orderitem_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_rev', models.IntegerField()),
            ],
        ),
    ]