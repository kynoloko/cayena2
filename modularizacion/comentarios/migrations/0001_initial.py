# Generated by Django 5.1.2 on 2024-10-17 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('score', models.IntegerField(default=3)),
                ('comentario', models.TextField(max_length=1000, null=True)),
            ],
        ),
    ]
