# Generated by Django 3.2.16 on 2023-01-20 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanri', '0016_auto_20230120_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesscount',
            name='page',
            field=models.CharField(max_length=100, verbose_name='Trang'),
        ),
    ]