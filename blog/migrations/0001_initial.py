# Generated by Django 4.0.1 on 2022-02-08 20:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('sumario', models.CharField(max_length=50)),
                ('nombre_imagen', models.CharField(max_length=50)),
                ('fecha', models.DateField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
                ('contenido', models.TextField(validators=[django.core.validators.MinLengthValidator(10)])),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.autor')),
                ('tags', models.ManyToManyField(to='blog.Tag')),
            ],
        ),
    ]
