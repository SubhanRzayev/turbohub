# Generated by Django 3.2.4 on 2022-03-26 23:19

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220326_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConditionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'ConditionCategories',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.CharField(blank=True, max_length=200, null=True)),
                ('mileage', models.CharField(blank=True, max_length=200, null=True)),
                ('car_image', models.ImageField(upload_to='media')),
                ('condition', models.CharField(blank=True, max_length=200, null=True)),
                ('brend', models.CharField(max_length=100)),
                ('dealer_comments', models.CharField(max_length=300)),
                ('slug', models.CharField(blank=True, max_length=300, null=True, unique=True, verbose_name='Slug')),
                ('kilometres', models.CharField(max_length=60)),
                ('colour', models.CharField(max_length=100)),
                ('transmission', models.CharField(max_length=100)),
                ('fuel_type', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=100)),
                ('engine', models.CharField(max_length=100)),
                ('drive_type', models.CharField(max_length=100)),
                ('in_depth_specifications', ckeditor_uploader.fields.RichTextUploadingField()),
                ('condition_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='condition_categories', to='core.conditioncategory')),
            ],
            options={
                'verbose_name_plural': 'Cars',
            },
        ),
        migrations.AlterField(
            model_name='image',
            name='cars_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars_image', to='core.car'),
        ),
        migrations.DeleteModel(
            name='Offers',
        ),
    ]