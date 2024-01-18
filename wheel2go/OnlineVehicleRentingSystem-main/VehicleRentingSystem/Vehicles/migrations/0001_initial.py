# Generated by Django 3.0.4 on 2021-03-03 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vehicle_name', models.CharField(max_length=60)),
                ('Vehicle_company', models.CharField(max_length=60)),
                ('Vehicle_model', models.CharField(max_length=60)),
                ('Vehicle_type', models.CharField(max_length=20)),
                ('Vehicle_fuel', models.CharField(max_length=10)),
                ('Vehicle_No_of_Seats', models.IntegerField()),
                ('Vehicle_color', models.CharField(max_length=20)),
                ('Vehicle_license_plate', models.CharField(max_length=30)),
                ('Vehicle_uploaded_by', models.CharField(max_length=100)),
                ('Vehicle_image1', models.ImageField(upload_to='img/Vehicle_images/')),
                ('Vehicle_image2', models.ImageField(upload_to='img/Vehicle_images/')),
                ('Vehicle_image3', models.ImageField(upload_to='img/Vehicle_images/')),
                ('isGeared', models.BooleanField()),
                ('Vehicle_description', models.CharField(max_length=1500)),
                ('Vehicle_Booked_date', models.DateField()),
                ('Vehicle_Return_date', models.DateField()),
                ('Vehicle_price', models.IntegerField()),
            ],
        ),
    ]
