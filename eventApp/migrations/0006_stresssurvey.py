# Generated by Django 4.0.1 on 2022-03-01 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventApp', '0005_userpreferences_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StressSurvey',
            fields=[
                ('SurveyID', models.AutoField(primary_key=True, serialize=False)),
                ('UserEmail', models.CharField(max_length=25)),
                ('SurveyValue', models.IntegerField()),
            ],
        ),
    ]
