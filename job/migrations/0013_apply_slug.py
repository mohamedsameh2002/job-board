# Generated by Django 4.2.2 on 2023-07-02 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_job_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]