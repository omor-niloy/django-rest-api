# Generated by Django 4.2 on 2023-04-08 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogapp', '0008_alter_breed_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='size',
            field=models.CharField(choices=[(1, 'Tiny'), (2, 'Small'), (3, 'Medium'), (4, 'Large')], max_length=40),
        ),
    ]
