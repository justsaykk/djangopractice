# Generated by Django 4.0.4 on 2022-05-07 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_category_todo_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]
