# Generated by Django 3.0.8 on 2020-09-13 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mate', '0003_auto_20200913_0219'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MateTask',
            new_name='MateQuest',
        ),
        migrations.RenameField(
            model_name='matequest',
            old_name='task1',
            new_name='quest1',
        ),
        migrations.RenameField(
            model_name='matequest',
            old_name='task10',
            new_name='quest10',
        ),
        migrations.RenameField(
            model_name='matequest',
            old_name='task11',
            new_name='quest11',
        ),
        migrations.RenameField(
            model_name='matequest',
            old_name='task12',
            new_name='quest12',
        ),
        migrations.RenameField(
            model_name='matequest',
            old_name='task2',
            new_name='quest2',
        ),
        migrations.RenameField(
            model_name='matequest',
            old_name='task3',
            new_name='quest3',
        ),
        migrations.RenameField(
            model_name='matequest',
            old_name='task4',
            new_name='quest4',
        ),
        migrations.RenameField(
            model_name='matequest',
            old_name='task5',
            new_name='quest5',
        ),
        migrations.RenameField(
            model_name='matequest',
            old_name='task6',
            new_name='quest6',
        ),
        migrations.RenameField(
            model_name='matequest',
            old_name='task7',
            new_name='quest7',
        ),
        migrations.RenameField(
            model_name='matequest',
            old_name='task8',
            new_name='quest8',
        ),
        migrations.RenameField(
            model_name='matequest',
            old_name='task9',
            new_name='quest9',
        ),
    ]