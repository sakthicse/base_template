# Generated by Django 2.2.3 on 2019-09-19 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='from_year',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='year',
            name='to_year',
            field=models.IntegerField(unique=True),
        ),
    ]