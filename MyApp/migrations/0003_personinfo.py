# Generated by Django 2.0.3 on 2021-03-24 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_auto_20210324_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonInfo',
            fields=[
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField(null=True)),
            ],
        ),
    ]