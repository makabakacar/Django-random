# Generated by Django 2.2.5 on 2020-12-07 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=128, verbose_name='密码')),
                ('gender', models.BooleanField(default=False, verbose_name='性别')),
                ('age', models.IntegerField(default=18, verbose_name='年龄')),
                ('mobile', models.CharField(max_length=11, null=True, verbose_name='手机号')),
            ],
            options={
                'db_table': 'tb_users',
            },
        ),
    ]
