# Generated by Django 5.1.7 on 2025-03-21 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
    ]
