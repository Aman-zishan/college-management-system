# Generated by Django 2.2.10 on 2021-03-31 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification',
            field=models.FileField(upload_to='menotification/'),
        ),
    ]