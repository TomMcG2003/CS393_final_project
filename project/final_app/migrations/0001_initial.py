# Generated by Django 4.2.16 on 2024-11-21 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('birthDay', models.DateField(null=True)),
                ('birthCity', models.CharField(max_length=50, null=True)),
                ('birthCountry', models.CharField(max_length=50, null=True)),
                ('weight', models.IntegerField(null=True)),
                ('height', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'Person',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('teamName', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Team',
            },
        ),
        migrations.CreateModel(
            name='TeamStats',
            fields=[
                ('teamstats_id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('divWinner', models.CharField(max_length=50, null=True)),
                ('wcWinner', models.CharField(max_length=50, null=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final_app.team')),
            ],
            options={
                'db_table': 'TeamStats',
            },
        ),
        migrations.CreateModel(
            name='Pitching',
            fields=[
                ('pitching_id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('wins', models.IntegerField(null=True)),
                ('loss', models.IntegerField(null=True)),
                ('games', models.IntegerField(null=True)),
                ('saves', models.IntegerField(null=True)),
                ('shutouts', models.IntegerField(null=True)),
                ('strikeouts', models.IntegerField(null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final_app.person')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final_app.team')),
            ],
            options={
                'db_table': 'Pitching',
            },
        ),
        migrations.CreateModel(
            name='Fielding',
            fields=[
                ('fielding_id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('putouts', models.IntegerField(null=True)),
                ('assists', models.IntegerField(null=True)),
                ('errors', models.IntegerField(null=True)),
                ('doublePlays', models.IntegerField(null=True)),
                ('passedBalls', models.IntegerField(null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final_app.person')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final_app.team')),
            ],
            options={
                'db_table': 'Fielding',
            },
        ),
        migrations.CreateModel(
            name='Batting',
            fields=[
                ('batting_id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('hits', models.IntegerField(null=True)),
                ('doubles', models.IntegerField(null=True)),
                ('triples', models.IntegerField(null=True)),
                ('homeruns', models.IntegerField(null=True)),
                ('strikeouts', models.IntegerField(null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final_app.person')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final_app.team')),
            ],
            options={
                'db_table': 'Batting',
            },
        ),
    ]