# Generated by Django 4.2.2 on 2023-06-19 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='jop_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], default='', max_length=20),
            preserve_default=False,
        ),
    ]
