# Generated by Django 3.2.23 on 2024-02-02 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerHome', '0007_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]