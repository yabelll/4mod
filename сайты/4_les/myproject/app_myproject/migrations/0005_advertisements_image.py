# Generated by Django 4.2.3 on 2023-08-26 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_myproject', '0004_advertisements_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisements',
            name='image',
            field=models.ImageField(default='', upload_to='adbertisements/', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
