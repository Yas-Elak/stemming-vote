# Generated by Django 2.2.10 on 2021-01-30 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('politico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totalvote',
            name='seance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='politico.Seance'),
        ),
    ]
