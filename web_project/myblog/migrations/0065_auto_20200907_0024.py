# Generated by Django 3.0.5 on 2020-09-06 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0064_auto_20200907_0023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='slug',
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='myblog.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(),
        ),
    ]
