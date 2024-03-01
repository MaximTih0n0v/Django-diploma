# Generated by Django 4.2.7 on 2024-03-01 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='end_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата и время окончания бронирования'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='start_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата и время начала бронирования'),
        ),
    ]