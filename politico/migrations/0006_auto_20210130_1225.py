# Generated by Django 2.2.10 on 2021-01-30 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('politico', '0005_auto_20210130_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totalvote',
            name='amendement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='politico.Amendement'),
        ),
        migrations.AlterField(
            model_name='totalvote',
            name='voting_point',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='politico.VotingPoint'),
        ),
    ]
