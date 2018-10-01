# Generated by Django 2.0.5 on 2018-10-01 03:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmsCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=30, verbose_name='手机号码')),
                ('code', models.CharField(max_length=12, verbose_name='验证码')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '短信验证码',
                'verbose_name_plural': '短信验证码',
            },
        ),
        migrations.RemoveField(
            model_name='vertifycode',
            name='phone',
        ),
        migrations.AddField(
            model_name='vertifycode',
            name='username',
            field=models.CharField(help_text='用户名', max_length=120, null=True, verbose_name='用户名'),
        ),
    ]