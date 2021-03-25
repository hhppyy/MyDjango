# Generated by Django 2.0.3 on 2021-03-25 03:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0005_testhan'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestTimer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creattime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('time', models.TimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
