# Generated by Django 4.2.5 on 2023-09-25 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_alter_landingpagecontent_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landingpagecontent',
            name='img',
            field=models.ImageField(upload_to='upload/', verbose_name=''),
        ),
    ]
