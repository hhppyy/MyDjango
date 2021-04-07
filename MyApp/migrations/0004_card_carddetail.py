# Generated by Django 2.0.3 on 2021-04-01 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(max_length=30, verbose_name='卡号')),
                ('card_user', models.CharField(max_length=30, verbose_name='姓名')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '银行卡_基本信息',
                'verbose_name_plural': '银行卡账户',
            },
        ),
        migrations.CreateModel(
            name='CardDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(max_length=30, verbose_name='手机号')),
                ('mail', models.CharField(max_length=30, verbose_name='邮箱')),
                ('city', models.CharField(max_length=30, verbose_name='城市')),
                ('address', models.CharField(max_length=30, verbose_name='详细地址')),
                ('card', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MyApp.Card', verbose_name='卡号')),
            ],
            options={
                'verbose_name': '账户_个人资料',
                'verbose_name_plural': '账户_个人资料',
            },
        ),
    ]