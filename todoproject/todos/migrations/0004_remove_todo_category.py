# Generated by Django 4.0.4 on 2022-05-07 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_category_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='category',
        ),
    ]
