# Generated by Django 3.0.3 on 2020-03-08 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorter', '0003_auto_20200308_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(max_length=1000, unique=True),
        ),
    ]
