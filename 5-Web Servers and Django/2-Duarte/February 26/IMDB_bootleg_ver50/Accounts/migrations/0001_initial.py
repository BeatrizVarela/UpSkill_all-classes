# Generated by Django 3.1.7 on 2021-02-26 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='profile/')),
                ('description', models.TextField()),
                ('birthdate', models.DateField()),
            ],
        ),
    ]
