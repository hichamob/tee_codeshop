# Generated by Django 3.2 on 2021-06-28 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_rename_createdat_review_createdatt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='createdAtt',
            new_name='createdAt',
        ),
    ]