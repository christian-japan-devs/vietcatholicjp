# Generated by Django 3.2.16 on 2023-01-20 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_prayer_prayer_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ceremony',
            name='type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='ceremonies', to='home.ceremonytype', verbose_name='Loại'),
        ),
    ]
