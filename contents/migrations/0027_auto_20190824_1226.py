# Generated by Django 2.2.4 on 2019-08-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0026_auto_20190824_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='document',
            field=models.FileField(blank=True, upload_to='certification'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='profile_pic'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='summary',
            field=models.CharField(max_length=200),
        ),
    ]
