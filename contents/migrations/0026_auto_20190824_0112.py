# Generated by Django 2.2.4 on 2019-08-24 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0025_seminar_link_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seminar',
            name='link_proof',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
