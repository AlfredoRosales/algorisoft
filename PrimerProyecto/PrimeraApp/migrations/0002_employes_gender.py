# Generated by Django 3.1 on 2020-09-25 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrimeraApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employes',
            name='gender',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
