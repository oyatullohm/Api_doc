# Generated by Django 4.0.6 on 2022-11-12 16:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mein', '0005_remove_table_section_td_remove_table_section_th_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='table_section',
            name='th',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
