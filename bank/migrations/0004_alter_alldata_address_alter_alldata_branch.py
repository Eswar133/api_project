# Generated by Django 5.0.6 on 2024-06-22 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_alldata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alldata',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='alldata',
            name='branch',
            field=models.CharField(max_length=200),
        ),
    ]
