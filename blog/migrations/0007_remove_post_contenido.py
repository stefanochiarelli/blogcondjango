# Generated by Django 4.0.1 on 2022-02-13 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_contenido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='contenido',
        ),
    ]
