# Generated by Django 2.0.3 on 2021-04-09 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0009_auto_20210409_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(default='', max_length=30, verbose_name='学号')),
                ('name', models.CharField(default='', max_length=30, verbose_name='姓名')),
                ('gender', models.CharField(choices=[('M', '男'), ('F', '女')], default='', max_length=10, verbose_name='性别')),
                ('age', models.IntegerField(default='', verbose_name='年龄')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
            },
        ),
    ]
