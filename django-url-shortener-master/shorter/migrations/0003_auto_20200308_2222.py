# Generated by Django 3.0.3 on 2020-03-08 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorter', '0002_auto_20200308_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='code',
            field=models.CharField(blank=True, max_length=1000, null=True, unique=True),
        ),
    ]
