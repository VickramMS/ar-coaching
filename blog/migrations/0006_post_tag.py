# Generated by Django 2.2.3 on 2019-07-18 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
