# Generated by Django 3.0.4 on 2020-09-16 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.TextField(),
        ),
    ]
