# Generated by Django 2.2.10 on 2021-01-30 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amendement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_nl', models.TextField(null=True)),
                ('title_fr', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parti_name', models.CharField(max_length=255)),
                ('parti_image', models.URLField(null=True)),
                ('parti_website_fr', models.URLField(null=True)),
                ('parti_website_nl', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seance_name', models.TextField(null=True)),
                ('seance_date', models.DateField()),
                ('seance_legislature', models.CharField(max_length=255, null=True)),
                ('seance_url', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TotalVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_cancelled', models.BooleanField(default=False)),
                ('number_of_oui', models.IntegerField(null=True)),
                ('number_of_non', models.IntegerField(null=True)),
                ('number_of_abstention', models.IntegerField(null=True)),
                ('amendement', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='politico.Amendement')),
                ('seance', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='politico.Seance')),
            ],
        ),
        migrations.CreateModel(
            name='VotingPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_title_nl', models.TextField(null=True)),
                ('point_title_fr', models.TextField(null=True)),
                ('seance', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='politico.Seance')),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter_name', models.CharField(max_length=255, null=True)),
                ('voter_url', models.URLField(null=True)),
                ('voter_website', models.URLField(null=True)),
                ('voter_email', models.CharField(max_length=255, null=True)),
                ('voter_image', models.URLField(null=True)),
                ('still_elected', models.BooleanField(default=True)),
                ('still_in_parti', models.BooleanField(default=True)),
                ('seances', models.ManyToManyField(to='politico.Seance')),
                ('voter_parti', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='politico.Parti')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_decision', models.IntegerField()),
                ('amendement', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='politico.Amendement')),
                ('seance', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='politico.Seance')),
                ('total_vote', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='politico.TotalVote')),
                ('voter', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='politico.Voter')),
                ('voting_point', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='politico.VotingPoint')),
            ],
        ),
        migrations.AddField(
            model_name='totalvote',
            name='voting_point',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='politico.VotingPoint'),
        ),
        migrations.AddField(
            model_name='amendement',
            name='seance',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='politico.Seance'),
        ),
        migrations.AddField(
            model_name='amendement',
            name='voting_point',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='politico.VotingPoint'),
        ),
    ]
