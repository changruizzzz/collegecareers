# Generated by Django 2.2.1 on 2019-10-06 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_job_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
