# Generated by Django 4.1.5 on 2023-01-24 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='img',
            field=models.ImageField(upload_to='feles/'),
        ),
    ]