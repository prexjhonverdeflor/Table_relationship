# Generated by Django 5.0.6 on 2024-05-15 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_bicsetup_item_code_bicsetup_level_1_bicsetup_level_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bicsetup',
            name='level_1',
            field=models.FloatField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='bicsetup',
            name='level_2',
            field=models.FloatField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='bicsetup',
            name='level_3',
            field=models.FloatField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='bicsetup',
            name='level_4',
            field=models.FloatField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='bicsetup',
            name='level_5',
            field=models.FloatField(blank=True, default=None),
        ),
    ]