# Generated by Django 5.0.3 on 2024-04-05 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_rename_schedule_attendance_schedule_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='subject_id',
        ),
    ]