# Generated by Django 5.0.7 on 2024-08-10 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_taskcategory_tasks'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='tasks',
            field=models.ManyToManyField(related_name='categories', to='category.taskcategory'),
        ),
    ]
