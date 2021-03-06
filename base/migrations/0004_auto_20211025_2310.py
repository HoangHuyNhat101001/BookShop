# Generated by Django 3.2.8 on 2021-10-25 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20211025_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookpage',
            field=models.FileField(upload_to='bookpage/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='coverpage',
            field=models.FileField(upload_to='coverpage/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.FileField(upload_to='category/'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='pic',
            field=models.FileField(upload_to='writer/'),
        ),
    ]
