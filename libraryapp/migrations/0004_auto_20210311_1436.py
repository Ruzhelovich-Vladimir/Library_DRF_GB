# Generated by Django 3.1.7 on 2021-03-11 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0003_auto_20210311_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biography',
            name='uuid',
        ),
        migrations.AlterField(
            model_name='biography',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='libraryapp.author', verbose_name='автор'),
        ),
    ]