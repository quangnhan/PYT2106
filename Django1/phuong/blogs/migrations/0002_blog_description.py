# Generated by Django 3.2.7 on 2021-09-16 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.CharField(default='Empty', max_length=100),
        ),
    ]