# Generated by Django 4.2.7 on 2023-11-24 18:35

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
                ('name', models.CharField(max_length=100)),
                ('secondname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.TextField()),
                ('bday', models.DateField()),
            ],
        ),
    ]
