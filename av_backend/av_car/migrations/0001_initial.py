# Generated by Django 5.0.2 on 2024-02-26 09:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('price', models.CharField(max_length=50)),
                ('price_usd', models.CharField(max_length=50)),
                ('image', models.TextField(max_length=200)),
                ('parameter', models.TextField(max_length=500)),
                ('description', models.TextField(max_length=500)),
                ('modification', models.TextField(max_length=500)),
                ('all_modification', models.TextField(max_length=500)),
                ('location', models.TextField(max_length=500)),
                ('comment', models.TextField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='av_car', to='av_car.category')),
            ],
            options={
                'ordering': ('name',),
                'index_together': {('id', 'name')},
            },
        ),
    ]
