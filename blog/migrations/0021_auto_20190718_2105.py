# Generated by Django 2.2.3 on 2019-07-18 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20190718_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='downloads',
            field=models.CharField(max_length=255),
        ),
    ]
