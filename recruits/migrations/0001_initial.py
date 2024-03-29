# Generated by Django 2.2.7 on 2019-11-05 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planet_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recruit_name', models.CharField(max_length=200)),
                ('recruit_age', models.IntegerField(default=0)),
                ('recruit_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ShadowHands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_test', models.IntegerField(default=0)),
                ('test', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sith',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sith_name', models.CharField(max_length=200)),
            ],
        ),
    ]
