# Generated by Django 3.2.16 on 2023-01-09 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20230108_2241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'ordering': ['-created_on'], 'verbose_name': 'Giới thiệu', 'verbose_name_plural': 'Giới thiệu'},
        ),
        migrations.AlterModelOptions(
            name='announcement',
            options={'ordering': ['-priority_choice', 'is_active', 'created_on'], 'verbose_name': 'Thông báo chung', 'verbose_name_plural': 'Thông báo chung'},
        ),
        migrations.AlterModelOptions(
            name='gospelcontent',
            options={'ordering': ['gospel', 'sequence', '-created_on'], 'verbose_name': 'Lời Chúa nội dung', 'verbose_name_plural': 'Lời Chúa nội dung'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on'], 'verbose_name': 'Bài viết-chủ đề', 'verbose_name_plural': 'Bài viết-chủ đề'},
        ),
        migrations.AlterModelOptions(
            name='postcontent',
            options={'ordering': ['post', 'sequence', '-created_on'], 'verbose_name': 'Bài viết-nội dung', 'verbose_name_plural': 'Bài viết-nội dung'},
        ),
        migrations.AlterModelOptions(
            name='posttype',
            options={'ordering': ['name'], 'verbose_name': 'Bài viết-phân loại', 'verbose_name_plural': 'Bài viết-phân loại'},
        ),
        migrations.RenameField(
            model_name='aboutus',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='announcement',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='letter',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='posttype',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='youtubevideo',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.AlterField(
            model_name='postcontent',
            name='chapter_summary',
            field=models.CharField(blank=True, default='', help_text='Không quá 500 ký tự', max_length=500, null=True, verbose_name='Tóm tắt'),
        ),
    ]
