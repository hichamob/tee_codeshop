# Generated by Django 3.2 on 2021-06-28 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_createdatt_review_createdat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='createdAt',
        ),
    ]
