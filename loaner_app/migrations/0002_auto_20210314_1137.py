# Generated by Django 3.1.7 on 2021-03-14 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loaner_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipment', to='loaner_app.members'),
        ),
    ]
