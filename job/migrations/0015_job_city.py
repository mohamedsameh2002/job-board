# Generated by Django 4.2.2 on 2023-07-03 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0014_apply_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
