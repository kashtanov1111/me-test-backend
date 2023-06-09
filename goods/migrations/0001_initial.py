# Generated by Django 4.1.7 on 2023-05-28 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('code', models.CharField(max_length=100)),
                ('supplier_name', models.CharField(max_length=300)),
                ('supplier_address', models.CharField(max_length=300)),
                ('supplier_phone', models.CharField(max_length=300)),
                ('is_bulk', models.BooleanField()),
                ('price', models.IntegerField()),
                ('dt_of_license', models.DateField()),
            ],
        ),
    ]
