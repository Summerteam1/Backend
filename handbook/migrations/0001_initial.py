# Generated by Django 3.2 on 2022-07-27 20:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pictures', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Essentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=256)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Handbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.PositiveSmallIntegerField(default=1)),
                ('weight_of_baby', models.PositiveSmallIntegerField()),
                ('height', models.PositiveSmallIntegerField()),
                ('weight_of_mom', models.PositiveSmallIntegerField()),
                ('nutrition', models.TextField()),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('advices', models.TextField()),
                ('fruit_img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('baby_img', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=255)),
                ('done', models.BooleanField(default=False)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]