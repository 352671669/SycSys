# Generated by Django 2.2.6 on 2020-04-15 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExcuteInfo',
            fields=[
                ('celery_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('context', models.CharField(max_length=255, unique=True)),
                ('excute_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='script',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('context', models.CharField(max_length=200)),
            ],
        ),
    ]
