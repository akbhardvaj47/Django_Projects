# Generated by Django 5.1.1 on 2025-05-12 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_colorvariant_sizevariant_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colorvariant',
            name='color_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='sizevariant',
            name='size_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
