# Generated by Django 2.0.5 on 2018-09-27 11:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_auto_20180927_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_name', models.CharField(max_length=12, verbose_name='活动icon名称')),
                ('name', models.CharField(max_length=30, verbose_name='活动名称')),
                ('description', models.CharField(max_length=200, verbose_name='描述')),
                ('icon_color', models.CharField(max_length=12, verbose_name='icon颜色')),
                ('_id', models.CharField(max_length=120, verbose_name='活动的id == key')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, help_text='添加时间', verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '活动',
                'verbose_name_plural': '活动',
            },
        ),
        migrations.CreateModel(
            name='DeliveryMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=12, verbose_name='颜色')),
                ('is_solid', models.BooleanField(default=True, verbose_name='是否专送')),
                ('text', models.CharField(max_length=120, verbose_name='内容信息')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, help_text='添加时间', verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '配送方式',
                'verbose_name_plural': '配送方式',
            },
        ),
        migrations.CreateModel(
            name='Identification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_number', models.CharField(max_length=200, verbose_name='工商号')),
                ('registered_address', models.CharField(max_length=200, verbose_name='工商地址')),
                ('operation_period', models.DateField(default=django.utils.timezone.now, verbose_name='操作时间')),
                ('licenses_scope', models.CharField(max_length=60, verbose_name='授权空间')),
                ('licenses_number', models.CharField(max_length=60, verbose_name='授权号')),
                ('licenses_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='授权日期')),
                ('legal_person', models.CharField(max_length=60, verbose_name='法人姓名')),
                ('identificate_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='注册日期')),
                ('identificate_agency', models.CharField(max_length=120, verbose_name='注册机构名称')),
                ('company_name', models.CharField(max_length=120, verbose_name='公司名称')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, help_text='添加时间', verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '商家认证信息',
                'verbose_name_plural': '商家认证信息',
            },
        ),
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_open', models.NullBooleanField(default=True, verbose_name='今天是否营业')),
                ('open_hour', models.CharField(max_length=12, verbose_name='开营时间')),
                ('close_hour', models.CharField(max_length=12, verbose_name='打烊时间')),
                ('description', models.CharField(max_length=120, verbose_name='描述')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, help_text='添加时间', verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '活动',
                'verbose_name_plural': '活动',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='店家名称')),
                ('address', models.CharField(max_length=200, verbose_name='店家地址')),
                ('latitude', models.FloatField(verbose_name='纬度')),
                ('longitude', models.FloatField(verbose_name='经度')),
                ('phone', models.CharField(max_length=60, verbose_name='电话')),
                ('status', models.SmallIntegerField(default=1, verbose_name='状态')),
                ('recent_order_num', models.IntegerField(verbose_name='订单数量')),
                ('rating_count', models.FloatField(verbose_name='评分数量')),
                ('rating', models.FloatField(verbose_name='综合评分')),
                ('promotion_info', models.CharField(max_length=120, verbose_name='提示信息')),
                ('is_new', models.BooleanField(default=True, verbose_name='是否是新店')),
                ('is_premium', models.BooleanField(default=False, verbose_name='是否溢价')),
                ('image_path', models.ImageField(upload_to='shop/images', verbose_name='商家图片')),
                ('float_minimum_order_amount', models.FloatField(verbose_name='最小减免')),
                ('float_delivery_fee', models.FloatField(verbose_name='配送费')),
                ('v', models.SmallIntegerField(default=0, help_text='数据的版本号', verbose_name='数据的版本号')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, help_text='添加时间', verbose_name='添加时间')),
                ('activities', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.Activities', verbose_name='活动')),
                ('category', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.Gategory', verbose_name='种类')),
                ('delivery_mode', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.DeliveryMode', verbose_name='配送方式')),
                ('identification', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.Identification', verbose_name='审核信息')),
            ],
            options={
                'verbose_name': '商家',
                'verbose_name_plural': '商家',
            },
        ),
        migrations.CreateModel(
            name='ShopLicense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catering_service_license_image', models.ImageField(upload_to='shop/service_license_image', verbose_name='营业执照')),
                ('business_license_image', models.ImageField(upload_to='shop/business_license_image', verbose_name='授权执照')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, help_text='添加时间', verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '商铺审核的图片',
                'verbose_name_plural': '商铺审核的图片',
            },
        ),
        migrations.CreateModel(
            name='Supports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=120, verbose_name='描述')),
                ('icon_color', models.CharField(max_length=12, verbose_name='颜色')),
                ('icon_name', models.CharField(max_length=12, verbose_name='icon名称')),
                ('name', models.CharField(max_length=60, verbose_name='名称')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, help_text='添加时间', verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '外卖的支持信息',
                'verbose_name_plural': '外卖的支持信息',
            },
        ),
        migrations.AddField(
            model_name='shop',
            name='license',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.ShopLicense', verbose_name='营业执照等'),
        ),
        migrations.AddField(
            model_name='shop',
            name='opening_hours',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.OpeningHours', verbose_name='营业时间'),
        ),
        migrations.AddField(
            model_name='shop',
            name='supports',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.Supports', verbose_name='保障'),
        ),
    ]
