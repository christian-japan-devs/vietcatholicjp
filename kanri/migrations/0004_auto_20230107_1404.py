# Generated by Django 3.2.16 on 2023-01-07 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kanri', '0003_auto_20230105_2056'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='father',
            options={'ordering': ('last_update_time',), 'verbose_name': 'Quý cha', 'verbose_name_plural': 'Quý cha'},
        ),
        migrations.AlterModelOptions(
            name='fatherandchurch',
            options={'ordering': ('is_active', 'father', 'church__name'), 'verbose_name': 'Cha tại nhà thờ', 'verbose_name_plural': 'Cha tại nhà thờ'},
        ),
        migrations.RemoveField(
            model_name='province',
            name='hiragana',
        ),
        migrations.RemoveField(
            model_name='region',
            name='hiragana',
        ),
        migrations.AddField(
            model_name='church',
            name='kanji',
            field=models.CharField(default='', help_text='Tên Kanji', max_length=200, verbose_name='Tên Kanji'),
        ),
        migrations.AddField(
            model_name='community',
            name='name_jp',
            field=models.CharField(default='', help_text='Tên nhóm', max_length=200, verbose_name='Tên tiếng Nhật'),
        ),
        migrations.AddField(
            model_name='facility',
            name='kanji',
            field=models.CharField(default='', max_length=50, verbose_name='Tên Kanji'),
        ),
        migrations.AddField(
            model_name='province',
            name='kanji',
            field=models.CharField(default='', max_length=50, verbose_name='Tên Kanji'),
        ),
        migrations.AddField(
            model_name='region',
            name='kanji',
            field=models.CharField(default='', max_length=50, verbose_name='Tên Kanji'),
        ),
        migrations.AlterField(
            model_name='church',
            name='name',
            field=models.CharField(default='', help_text='Tên Hiragana', max_length=200, verbose_name='Tên Hiragana'),
        ),
        migrations.AlterField(
            model_name='community',
            name='name',
            field=models.CharField(help_text='Tên nhóm', max_length=200, verbose_name='Tên nhóm'),
        ),
        migrations.AlterField(
            model_name='facility',
            name='name',
            field=models.CharField(help_text='Tên', max_length=200, verbose_name='Tên Hiragana'),
        ),
        migrations.AlterField(
            model_name='province',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Tên hiragana'),
        ),
        migrations.AlterField(
            model_name='province',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kanri.region', verbose_name='Vùng'),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Tên hiragana'),
        ),
        migrations.AlterField(
            model_name='region',
            name='nation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kanri.country', verbose_name='Quốc gia'),
        ),
        migrations.AlterUniqueTogether(
            name='father',
            unique_together={('user', 'address')},
        ),
        migrations.RemoveField(
            model_name='father',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='father',
            name='image',
        ),
        migrations.RemoveField(
            model_name='father',
            name='saint_name',
        ),
    ]