# Generated by Django 2.0.5 on 2018-09-29 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0008_auto_20180929_1413'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activities',
            options={'verbose_name': '店铺活动', 'verbose_name_plural': '店铺活动'},
        ),
        migrations.AlterModelOptions(
            name='openinghours',
            options={'verbose_name': '营业时间', 'verbose_name_plural': '营业时间'},
        ),
    ]
