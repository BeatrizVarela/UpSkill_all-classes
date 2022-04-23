# Generated by Django 3.1.7 on 2021-03-18 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMDB_APP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, null=True, related_name='movies', to='IMDB_APP.Actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(),
        ),
    ]
