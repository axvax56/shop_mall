# Generated by Django 4.2.2 on 2023-06-17 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=64)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '고객',
                'verbose_name_plural': '고객',
                'db_table': 'my_user',
            },
        ),
    ]
