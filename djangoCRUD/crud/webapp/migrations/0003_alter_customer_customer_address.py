# Generated by Django 5.0.6 on 2024-05-15 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_customer_remove_bicsetup_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_address',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
