# Generated by Django 4.1.7 on 2023-03-02 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_type_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='type',
            field=models.ManyToManyField(related_name='task_type', to='webapp.type', verbose_name='Тип задачи'),
        ),
    ]
