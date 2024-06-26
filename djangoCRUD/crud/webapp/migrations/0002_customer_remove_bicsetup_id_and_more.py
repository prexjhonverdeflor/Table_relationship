# Generated by Django 5.0.6 on 2024-05-15 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_fullname', models.CharField(default='Fullname', max_length=255)),
                ('customer_firstname', models.CharField(default='Firstname', max_length=255)),
                ('customer_middlename', models.CharField(blank=True, max_length=255, null=True)),
                ('customer_lastname', models.CharField(default='Lastname', max_length=255)),
                ('customer_address', models.TextField(blank=True)),
                ('customer_level', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='bicsetup',
            name='id',
        ),
        migrations.AlterField(
            model_name='bicsetup',
            name='product_code',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
