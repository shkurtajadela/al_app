# Generated by Django 3.2.5 on 2023-02-23 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_formquestion_revrating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formquestion',
            name='revRating',
        ),
    ]