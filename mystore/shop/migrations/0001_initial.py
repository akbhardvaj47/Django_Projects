# Generated by Django 5.1.1 on 2025-05-07 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('product_desc', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
