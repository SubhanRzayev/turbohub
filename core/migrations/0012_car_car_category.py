# Generated by Django 3.2.4 on 2022-03-29 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_car_car_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car_categories', to='core.carcategory'),
        ),
    ]