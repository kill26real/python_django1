# Generated by Django 4.1.5 on 2023-01-22 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0006_alter_news_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
