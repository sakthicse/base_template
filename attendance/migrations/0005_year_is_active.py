# Generated by Django 2.2.3 on 2019-09-24 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_attendance_hostelstudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='year',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
