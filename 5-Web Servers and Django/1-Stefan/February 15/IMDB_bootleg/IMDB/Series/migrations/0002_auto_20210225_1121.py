# Generated by Django 3.1.6 on 2021-02-25 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Series', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]