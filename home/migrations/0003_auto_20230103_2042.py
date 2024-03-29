# Generated by Django 3.2.16 on 2023-01-03 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kanri', '0001_initial'),
        ('home', '0002_aboutus_created_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=100, verbose_name='Tên Ngôn ngữ')),
                ('language_code', models.CharField(max_length=3, verbose_name='Mã')),
                ('language_flag_small_url', models.ImageField(blank=True, null=True, upload_to='flags', verbose_name='Hình ảnh')),
                ('language_flag_medium_url', models.ImageField(blank=True, null=True, upload_to='flags', verbose_name='Hình ảnh')),
            ],
        ),
        migrations.CreateModel(
            name='MassDateSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=300, verbose_name='Tiêu đề')),
                ('slug', models.CharField(blank=True, default='', max_length=400, null=True, verbose_name='slug')),
                ('date', models.DateField(auto_now=True, null=True, verbose_name='Ngày')),
            ],
            options={
                'verbose_name': 'Lịch Lễ',
                'verbose_name_plural': 'Lịch Lễ',
                'ordering': ['-date'],
            },
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='short_introduce',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='excerpt',
            field=tinymce.models.HTMLField(default='', verbose_name='Tóm tắt'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='Nội dung'),
        ),
        migrations.CreateModel(
            name='MassTimeSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(default='', max_length=300, verbose_name='Giờ')),
                ('notes', tinymce.models.HTMLField(blank=True, default='', null=True, verbose_name='Ghi chú')),
                ('church', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mass_church', to='kanri.church', verbose_name='Nhà thờ')),
                ('date_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.massdateschedule', verbose_name='Thánh Lễ')),
                ('father', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mass_father', to='kanri.father', verbose_name='Cha')),
                ('province', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mass_province', to='kanri.province', verbose_name='Tỉnh')),
            ],
            options={
                'verbose_name': 'Lịch Lễ chi tiết',
                'verbose_name_plural': 'Lịch Lễ chi tiết',
                'ordering': ['-date_schedule'],
            },
        ),
        migrations.CreateModel(
            name='ConfessSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Bắt đầu từ')),
                ('to_date_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Đến khi')),
                ('notes', models.CharField(blank=True, default='', max_length=500, verbose_name='Ghi chú')),
                ('publish', models.BooleanField(blank=True, default=True, verbose_name='Công khai')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created on')),
                ('church', models.ForeignKey(blank=True, help_text='chọn Nhà thờ', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confess_church', to='kanri.church')),
                ('father', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kanri.father', verbose_name='Cha')),
            ],
            options={
                'verbose_name': 'Lịch giải tội',
                'verbose_name_plural': 'Lịch giải tội',
                'ordering': ['-from_date_time'],
            },
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('slug', models.CharField(max_length=200, verbose_name='Slug')),
                ('imageUrl', models.ImageField(blank=True, null=True, upload_to='web_images/announ', verbose_name='Image')),
                ('excerpt', tinymce.models.HTMLField(blank=True, default='', null=True, verbose_name='short description')),
                ('content', tinymce.models.HTMLField()),
                ('isActive', models.BooleanField(blank=True, default=True, verbose_name='Publish')),
                ('from_date', models.DateField(default=django.utils.timezone.now, verbose_name='From Date')),
                ('to_date', models.DateField(default=django.utils.timezone.now, verbose_name='To Date')),
                ('event_date_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Event date time')),
                ('google_map_link', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Google Map Link')),
                ('register_link', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Register Link')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created on')),
                ('author', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('language', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.language')),
                ('updated_user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Thông báo chung',
                'verbose_name_plural': 'Thông báo chung',
                'ordering': ['created_on'],
            },
        ),
    ]
