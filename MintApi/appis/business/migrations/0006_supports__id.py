# Generated by Django 2.0.5 on 2018-09-27 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0005_auto_20180927_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='supports',
            name='_id',
            field=models.CharField(default=666, max_length=120, verbose_name='保障的id == key'),
            preserve_default=False,
        ),
    ]
