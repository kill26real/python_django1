# Generated by Django 4.1.5 on 2023-01-22 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0007_news_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='tag',
            field=models.CharField(blank=True, max_length=30, verbose_name='Тэг'),
        ),
    ]
