# Generated by Django 4.0.4 on 2022-07-09 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0010_patients_heart_rate_alter_patients_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hotel_Main_Img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]