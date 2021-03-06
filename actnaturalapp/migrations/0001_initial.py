# Generated by Django 3.0.7 on 2020-06-10 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('image', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'Animal',
                'verbose_name_plural': 'Animals',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.CreateModel(
            name='EnrichmentItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=500)),
                ('is_manager_approved', models.BooleanField()),
                ('is_vet_approved', models.BooleanField()),
                ('image', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'EnrichmentItem',
                'verbose_name_plural': 'EnrichmentItems',
            },
        ),
        migrations.CreateModel(
            name='EnrichmentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'EnrichmentType',
                'verbose_name_plural': 'EnrichmentTypes',
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Species',
                'verbose_name_plural': 'Species',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='EnrichmentLogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('note', models.CharField(max_length=500)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actnaturalapp.Animal')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='actnaturalapp.Employee')),
                ('enrichment_item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='actnaturalapp.EnrichmentItem')),
            ],
            options={
                'verbose_name': 'EnrichmentLogEntry',
                'verbose_name_plural': 'EnrichmentLogEntries',
            },
        ),
        migrations.AddField(
            model_name='enrichmentitem',
            name='enrichment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actnaturalapp.EnrichmentType'),
        ),
        migrations.AddField(
            model_name='enrichmentitem',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actnaturalapp.Team'),
        ),
        migrations.AddField(
            model_name='employee',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actnaturalapp.Team'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='AnimalNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actnaturalapp.Animal')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='actnaturalapp.Employee')),
            ],
            options={
                'verbose_name': 'AnimalNote',
                'verbose_name_plural': 'AnimalNotes',
            },
        ),
        migrations.CreateModel(
            name='AnimalEnrichmentItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actnaturalapp.Animal')),
                ('enrichment_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actnaturalapp.EnrichmentItem')),
            ],
            options={
                'verbose_name': 'AnimalEnrichmentItem',
                'verbose_name_plural': 'AnimalEnrichmentItems',
            },
        ),
        migrations.AddField(
            model_name='animal',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actnaturalapp.Species'),
        ),
        migrations.AddField(
            model_name='animal',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actnaturalapp.Team'),
        ),
    ]
