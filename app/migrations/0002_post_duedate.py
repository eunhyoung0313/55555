# Generated by Django 3.0.6 on 2020-05-18 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='duedate',
            field=models.DateTimeField(null=True),
        ),
    ]
