# Generated by Django 3.0.6 on 2021-09-24 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210924_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_end',
            field=models.DateField(verbose_name='Date'),
        ),
    ]