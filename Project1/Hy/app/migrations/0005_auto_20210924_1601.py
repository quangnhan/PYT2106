# Generated by Django 3.0.6 on 2021-09-24 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210924_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_end',
            field=models.DateTimeField(),
        ),
    ]
