# Generated by Django 3.0.3 on 2020-05-04 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inside',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
