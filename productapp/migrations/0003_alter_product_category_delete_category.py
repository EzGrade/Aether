# Generated by Django 5.0.2 on 2024-04-19 09:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoryapp', '0001_initial'),
        ('productapp', '0002_product_user_productimage_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='categoryapp.category'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
