# Generated by Django 2.1.4 on 2019-06-03 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=320)),
                ('founding_date', models.DateField(verbose_name='date of founding')),
                ('origin_country', models.CharField(max_length=128)),
                ('members', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArtistType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('lenght_seconds', models.IntegerField()),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='RecordType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('composer', models.CharField(max_length=128)),
                ('lyrics', models.TextField(null=True)),
                ('artists', models.ManyToManyField(to='records.Artist')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.Record')),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='record_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.RecordType'),
        ),
        migrations.AddField(
            model_name='artist',
            name='artist_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.ArtistType'),
        ),
    ]
