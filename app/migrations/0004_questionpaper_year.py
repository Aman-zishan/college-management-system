# Generated by Django 2.2.10 on 2021-04-02 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210402_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionpaper',
            name='year',
            field=models.IntegerField(default=2019),
        ),
    ]
