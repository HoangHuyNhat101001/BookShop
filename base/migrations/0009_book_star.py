# Generated by Django 3.2.8 on 2021-10-31 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_book_review_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='star',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
