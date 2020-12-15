# Generated by Django 3.1.1 on 2020-09-18 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Counsel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who', models.CharField(max_length=10, verbose_name='상담방법')),
                ('how', models.CharField(max_length=10, verbose_name='상담형태')),
                ('teacher', models.CharField(max_length=10, verbose_name='상담자')),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='USERNAME')),
            ],
        ),
    ]
