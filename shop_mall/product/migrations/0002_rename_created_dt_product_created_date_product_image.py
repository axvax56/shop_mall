# Generated by Django 4.2.2 on 2023-06-17 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='created_dt',
            new_name='created_date',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='product/%Y/%m/%d'),
        ),
    ]
