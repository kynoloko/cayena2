# Generated by Django 5.1.2 on 2024-10-18 16:07

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('emal', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabecera', models.CharField(max_length=255)),
                ('cuerpotexto', models.TextField()),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('promedio', models.IntegerField(default=5)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.autor')),
            ],
        ),
    ]
