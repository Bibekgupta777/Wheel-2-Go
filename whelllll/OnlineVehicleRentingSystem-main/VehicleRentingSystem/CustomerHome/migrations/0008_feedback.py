# Generated by Django 4.1.2 on 2024-02-02 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerHome', '0007_remove_customer_customer_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('rating', models.IntegerField()),
                ('feedback_text', models.TextField()),
            ],
        ),
    ]
