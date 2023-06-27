# Generated by Django 3.2.19 on 2023-06-27 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='like',
            constraint=models.UniqueConstraint(fields=('news', 'user'), name='unique_relationships'),
        ),
    ]
