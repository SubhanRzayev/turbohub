# Generated by Django 3.2.4 on 2022-03-28 23:03

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20220328_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='working_hours',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='asdasda'),
            preserve_default=False,
        ),
    ]