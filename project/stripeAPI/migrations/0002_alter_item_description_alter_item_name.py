# Generated by Django 4.1.1 on 2022-09-08 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripeAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]