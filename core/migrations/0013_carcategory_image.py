# Generated by Django 3.2.4 on 2022-03-29 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_car_car_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='carcategory',
            name='image',
            field=models.ImageField(default='mercedes.png', upload_to='media'),
            preserve_default=False,
        ),
    ]