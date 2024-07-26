# Generated by Django 5.0.7 on 2024-07-24 01:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(max_length=100)),
                ('given_names', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploaded_images/')),
                ('gender', models.CharField(max_length=10)),
                ('nationality', models.CharField(max_length=50)),
                ('occupation_name', models.CharField(max_length=100)),
                ('travel_document_number', models.CharField(max_length=50)),
                ('travel_document_expiry_date', models.DateField()),
                ('visa_grant_date', models.DateField()),
                ('visa_use_by_date', models.DateField()),
                ('visa_application_number', models.CharField(max_length=20)),
                ('visa_number', models.CharField(max_length=20)),
                ('visa_expiry_date', models.DateField(editable=False)),
                ('length_of_stay', models.CharField(max_length=20)),
                ('number_of_entries', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VisaStream.application')),
            ],
        ),
    ]
