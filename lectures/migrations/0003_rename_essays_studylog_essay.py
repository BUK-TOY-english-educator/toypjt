# Generated by Django 3.2.12 on 2022-05-09 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0002_studylog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studylog',
            old_name='essays',
            new_name='essay',
        ),
    ]