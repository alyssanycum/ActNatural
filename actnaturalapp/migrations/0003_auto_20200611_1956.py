# Generated by Django 3.0.7 on 2020-06-11 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actnaturalapp', '0002_auto_20200611_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
