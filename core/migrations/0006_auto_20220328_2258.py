# Generated by Django 3.2.4 on 2022-03-28 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220328_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='call_us',
            field=models.CharField(default='+1 (289) 788-9196', max_length=200),
        ),
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(default='(123) 456-7890', max_length=200),
        ),
    ]
