# Generated by Django 4.0.5 on 2022-06-27 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_description',
            field=models.CharField(default='Basic Description', max_length=266),
        ),
    ]
