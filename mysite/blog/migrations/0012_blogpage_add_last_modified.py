# Generated by Django 3.1.12 on 2021-10-16 13:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('blog', '0012_blogpage_last_updated'), ('blog', '0013_remove_blogpage_last_updated'), ('blog', '0014_blogpage_last_modified'), ('blog', '0015_auto_20211016_1449')]

    dependencies = [
        ('blog', '0011_auto_20201114_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='last_modified',
            field=models.DateField(default=datetime.date(2021, 10, 16), verbose_name='Last updated'),
        ),
    ]
