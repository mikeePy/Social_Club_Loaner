# Generated by Django 3.1.7 on 2021-03-15 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loaner_app', '0002_auto_20210314_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='loaner_app.members'),
        ),
    ]
