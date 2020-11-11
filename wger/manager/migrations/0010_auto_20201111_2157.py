# Generated by Django 3.1.3 on 2020-11-11 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0009_setting_rpe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='rpe',
            field=models.DecimalField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], decimal_places=1, default=5, max_digits=3, null=True, verbose_name='rpe'),
        ),
    ]
