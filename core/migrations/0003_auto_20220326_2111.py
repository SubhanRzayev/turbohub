# Generated by Django 3.2.4 on 2022-03-26 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220326_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='offers',
            name='slug',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True, verbose_name='Slug'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('cars_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars_image', to='core.offers')),
            ],
        ),
    ]