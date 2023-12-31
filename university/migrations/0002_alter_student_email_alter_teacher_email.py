# Generated by Django 5.0 on 2023-12-31 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=30, verbose_name='Email студента'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=30, verbose_name='Email учителя'),
        ),
    ]
