# Generated by Django 5.0 on 2023-12-09 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_gall_gallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='button1',
        ),
        migrations.AlterField(
            model_name='gallery',
            name='button',
            field=models.TextField(max_length=50, verbose_name='button name'),
        ),
    ]
