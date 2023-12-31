# Generated by Django 4.1.5 on 2023-01-31 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0003_remove_blogpost_img_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'image', 'verbose_name_plural': 'images'},
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date of publish'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='text',
            field=models.TextField(default='', verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(upload_to='files/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='image',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.blogpost', verbose_name='post'),
        ),
    ]
