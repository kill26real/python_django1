# Generated by Django 4.1.5 on 2023-01-18 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Заголовок')),
                ('text', models.TextField(default='', verbose_name='Содержимое')),
                ('publisher', models.CharField(max_length=30, verbose_name='Кто опубликовал')),
                ('published_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'permissions': {('can_publish', 'Может публиковать')},
            },
        ),
    ]