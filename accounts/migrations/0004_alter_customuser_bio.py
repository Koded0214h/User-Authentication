# Generated by Django 5.1.3 on 2025-01-12 13:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_bio_customuser_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='bio',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
