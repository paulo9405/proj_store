# Generated by Django 3.2.7 on 2021-09-19 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='categories',
            unique_together={('name',)},
        ),
    ]