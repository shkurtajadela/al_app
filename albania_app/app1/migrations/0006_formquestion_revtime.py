# Generated by Django 4.1.7 on 2023-03-14 09:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_remove_formquestion_revrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='formquestion',
            name='revTime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]