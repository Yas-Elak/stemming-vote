# Generated by Django 2.2.10 on 2021-01-30 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('politico', '0004_auto_20210130_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amendement',
            name='seance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='politico.Seance'),
        ),
        migrations.AlterField(
            model_name='votingpoint',
            name='seance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='politico.Seance'),
        ),
    ]