# Generated by Django 2.0.5 on 2018-09-27 07:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_in_serving', models.BooleanField(default=True, verbose_name='是否在服务区内')),
                ('image_url', models.ImageField(upload_to='gategory/images', verbose_name='图片')),
                ('icon_url', models.ImageField(upload_to='gategory/icons', verbose_name='图标')),
                ('description', models.CharField(max_length=200, verbose_name='描述')),
                ('title_color', models.CharField(max_length=30, verbose_name='颜色')),
                ('title', models.CharField(max_length=60, verbose_name='标题')),
                ('link', models.URLField(verbose_name='链接')),
                ('v', models.SmallIntegerField(verbose_name='版本号')),
                ('add_time', models.DateTimeField(default=datetime.datetime(2018, 9, 27, 7, 58, 35, 969406, tzinfo=utc), verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '商家分类',
                'verbose_name_plural': '商家分类',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geohash', models.CharField(max_length=120, verbose_name='经度,纬度')),
                ('name', models.CharField(max_length=200, verbose_name='显示地址')),
                ('address', models.CharField(max_length=200, verbose_name='地址')),
                ('city', models.CharField(max_length=60, verbose_name='城市')),
                ('longitude', models.FloatField(verbose_name='纬度')),
                ('latitude', models.FloatField(verbose_name='经度')),
            ],
            options={
                'verbose_name': '获取位置的接口',
                'verbose_name_plural': '获取位置的接口',
            },
        ),
    ]
