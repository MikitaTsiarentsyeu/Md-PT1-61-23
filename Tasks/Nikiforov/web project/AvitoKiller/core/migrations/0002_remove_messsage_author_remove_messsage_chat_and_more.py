# Generated by Django 4.2.1 on 2023-06-16 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messsage',
            name='author',
        ),
        migrations.RemoveField(
            model_name='messsage',
            name='chat',
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
        migrations.DeleteModel(
            name='Messsage',
        ),
    ]