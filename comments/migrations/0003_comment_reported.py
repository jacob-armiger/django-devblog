# Generated by Django 2.2.4 on 2019-08-21 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20190730_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='reported',
            field=models.BooleanField(default=False),
        ),
    ]