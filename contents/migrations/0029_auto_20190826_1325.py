# Generated by Django 2.2.4 on 2019-08-26 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0028_auto_20190824_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='document',
            field=models.FileField(blank=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]