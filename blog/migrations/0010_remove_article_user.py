# Generated by Django 2.2.3 on 2019-08-06 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190806_0353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='user',
        ),
    ]
