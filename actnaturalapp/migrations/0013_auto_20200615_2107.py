# Generated by Django 3.0.7 on 2020-06-15 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actnaturalapp', '0012_auto_20200615_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalnote',
            name='animal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actnaturalapp.Animal'),
        ),
    ]
