# Generated by Django 3.2.7 on 2021-09-19 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_categories_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='country',
            unique_together={('name',)},
        ),
    ]