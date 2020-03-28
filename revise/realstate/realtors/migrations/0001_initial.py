# Generated by Django 3.0.4 on 2020-03-24 03:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('description', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=20)),
                ('is_mvp', models.BooleanField(default=False)),
                ('email', models.CharField(max_length=70)),
                ('hire_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]