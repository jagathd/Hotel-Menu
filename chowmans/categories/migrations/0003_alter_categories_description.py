# Generated by Django 4.2.9 on 2024-01-10 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_categories_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]