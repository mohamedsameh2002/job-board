# Generated by Django 4.2.2 on 2023-06-22 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='job',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='job.job'),
            preserve_default=False,
        ),
    ]
