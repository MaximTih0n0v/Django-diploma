# Generated by Django 4.2.7 on 2024-03-02 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, max_length=18, null=True, verbose_name='Телефон'),
        ),
    ]
