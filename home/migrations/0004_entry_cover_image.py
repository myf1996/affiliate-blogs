# Generated by Django 4.1.1 on 2022-09-20 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_categories_isactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='cover_image',
            field=models.ImageField(blank=True, upload_to='blog/images'),
        ),
    ]
