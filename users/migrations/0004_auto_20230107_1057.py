# Generated by Django 3.2.16 on 2023-01-07 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customusermodel_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusermodel',
            name='full_name',
            field=models.CharField(default='', max_length=100, verbose_name='Họ tên'),
        ),
        migrations.AddField(
            model_name='customusermodel',
            name='image',
            field=models.ImageField(default='default.jpg', null=True, upload_to='images/users', verbose_name='Hình đại diện'),
        ),
        migrations.AddField(
            model_name='customusermodel',
            name='saint_name',
            field=models.CharField(default='', max_length=100, verbose_name='Tên thánh'),
        ),
        migrations.AlterUniqueTogether(
            name='profile',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='saint_name',
        ),
    ]
