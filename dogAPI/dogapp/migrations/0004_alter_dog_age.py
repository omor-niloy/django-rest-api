# Generated by Django 4.2 on 2023-04-08 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogapp', '0003_alter_dog_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='age',
            field=models.CharField(max_length=100),
        ),
    ]
