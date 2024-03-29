# Generated by Django 3.2.16 on 2023-01-11 08:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kanri', '0010_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='churchimages',
            options={'ordering': ['created_on'], 'verbose_name': 'Nhà thờ ảnh', 'verbose_name_plural': 'Nhà thờ ảnh'},
        ),
        migrations.AlterModelOptions(
            name='community',
            options={'ordering': ['name', 'province', 'created_on'], 'verbose_name': 'Cộng đoàn, nhóm', 'verbose_name_plural': 'Cộng đoàn, nhóm'},
        ),
        migrations.AlterModelOptions(
            name='facility',
            options={'ordering': ['name'], 'verbose_name': 'Facility', 'verbose_name_plural': 'Facilities'},
        ),
        migrations.AlterModelOptions(
            name='father',
            options={'ordering': ('created_on',), 'verbose_name': 'User-Quý cha', 'verbose_name_plural': 'User-Quý cha'},
        ),
        migrations.AlterModelOptions(
            name='representative',
            options={'ordering': ('-created_on',), 'verbose_name': 'User-Representative', 'verbose_name_plural': 'User-Representatives'},
        ),
        migrations.AlterModelOptions(
            name='representativeandcommunity',
            options={'ordering': ('is_active', 'community', 'responsibility', 'representative', '-from_date', '-to_date'), 'verbose_name': 'Communnity and representative', 'verbose_name_plural': 'Master-Communnity and representatives'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ('user__username', 'user__email'), 'verbose_name': 'User-User profile', 'verbose_name_plural': 'User-User profiles'},
        ),
        migrations.AddField(
            model_name='church',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, help_text='Lần cuối cập nhật', verbose_name='Ngày cập nhật'),
        ),
        migrations.AddField(
            model_name='church',
            name='updated_user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='church_updated_user', to=settings.AUTH_USER_MODEL, verbose_name='Người cập nhật'),
        ),
        migrations.AlterField(
            model_name='churchimages',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo'),
        ),
        migrations.AlterField(
            model_name='representativeandcommunity',
            name='from_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Từ ngày'),
        ),
        migrations.AlterField(
            model_name='representativeandcommunity',
            name='to_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Đến ngày'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='code_created_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Thời gian tạo mã'),
        ),
    ]
