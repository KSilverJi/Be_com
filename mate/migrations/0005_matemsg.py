# Generated by Django 3.0.8 on 2020-09-13 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mate', '0004_auto_20200913_1823'),
    ]

    operations = [
        migrations.CreateModel(
            name='MateMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=400)),
                ('mate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mate.Mate')),
            ],
        ),
    ]
