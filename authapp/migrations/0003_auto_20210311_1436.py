# Generated by Django 3.1.7 on 2021-03-11 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20210302_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'M'), ('W', 'Ж')], max_length=1, verbose_name='пол'),
        ),
    ]
