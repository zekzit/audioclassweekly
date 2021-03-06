# Generated by Django 3.1.7 on 2021-02-23 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_class_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AudioClassWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_name', models.CharField(max_length=200)),
                ('audio_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audios.audioclass')),
            ],
        ),
    ]
