# Generated by Django 2.2.7 on 2019-11-06 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruits', '0008_auto_20191106_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruit',
            name='recruit_test',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
