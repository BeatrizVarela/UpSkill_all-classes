# Generated by Django 3.1.7 on 2021-03-02 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actor', to='Staff.staff'),
        ),
        migrations.AlterField(
            model_name='director',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='director', to='Staff.staff'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writer', to='Staff.staff'),
        ),
    ]
