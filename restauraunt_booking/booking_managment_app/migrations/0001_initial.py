# Generated by Django 5.0.2 on 2024-03-09 13:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('db_users_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('is_booked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_of_people', models.IntegerField()),
                ('booking_data', models.DateTimeField()),
                ('valid_until', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_users_app.user')),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_managment_app.place')),
            ],
            options={
                'unique_together': {('user', 'number', 'count_of_people', 'booking_data', 'valid_until')},
            },
        ),
    ]
