# Generated by Django 2.0.3 on 2018-03-18 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_publish',
            field=models.BooleanField(default=0),
        ),
    ]
