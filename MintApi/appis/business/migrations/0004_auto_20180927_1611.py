# Generated by Django 2.0.5 on 2018-09-27 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_auto_20180927_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gategory',
            name='icon_url',
            field=models.ImageField(default='', help_text='图标', upload_to='gategory/icons', verbose_name='图标'),
        ),
        migrations.AlterField(
            model_name='gategory',
            name='link',
            field=models.URLField(default='', help_text='链接', verbose_name='链接'),
        ),
        migrations.AlterField(
            model_name='gategory',
            name='title_color',
            field=models.CharField(default='', help_text='颜色', max_length=30, verbose_name='颜色'),
        ),
    ]
