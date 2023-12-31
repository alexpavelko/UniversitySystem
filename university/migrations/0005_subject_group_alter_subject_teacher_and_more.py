# Generated by Django 5.0 on 2024-01-01 14:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0004_alter_subject_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='university.group', verbose_name='Группа'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subject',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.teacher', verbose_name='Преподаватель, который ведет предмет'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=30, verbose_name='Email преподавателя'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='job_position',
            field=models.CharField(choices=[('Ассистент', 'Ассистент'), ('Старший Преподаватель', 'Старший Преподаватель'), ('Доцент', 'Доцент'), ('Профессор', 'Профессор')], max_length=40, verbose_name='Должность'),
        ),
    ]
