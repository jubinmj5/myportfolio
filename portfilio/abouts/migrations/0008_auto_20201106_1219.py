# Generated by Django 3.1.2 on 2020-11-06 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abouts', '0007_auto_20201106_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
