# Generated by Django 4.1.4 on 2023-01-21 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductId', models.IntegerField()),
                ('ProductName', models.CharField(max_length=15)),
                ('CategoryId', models.IntegerField()),
                ('CategoryName', models.CharField(max_length=30)),
            ],
        ),
    ]
