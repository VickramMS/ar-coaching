# Generated by Django 2.2.3 on 2019-08-27 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_auto_20190827_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.CharField(choices=[('PG TRB', 'PG TRB'), ('POLY TRB', 'POLY TRB'), ('ENGG TRB', 'ENGR-TRB'), ('TNSET', 'TNSET'), ('GATE', 'GATE'), ('SAMPLE MATERIALS', 'SAMLPLE MATERIALS')], max_length=255),
        ),
    ]
