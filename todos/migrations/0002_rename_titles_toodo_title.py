# Generated by Django 3.2 on 2022-03-27 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='toodo',
            old_name='titles',
            new_name='title',
        ),
    ]
