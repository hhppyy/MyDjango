# Generated by Django 2.0.3 on 2021-03-25 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_personinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='personinfo',
            name='add',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='personinfo',
            name='email',
            field=models.CharField(default='123@qq.com', max_length=30),
        ),
    ]
