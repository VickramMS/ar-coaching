# Generated by Django 2.2.3 on 2019-07-18 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190718_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.URLField(blank=True, max_length=512),
        ),
    ]
