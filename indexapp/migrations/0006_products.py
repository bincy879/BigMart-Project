# Generated by Django 4.1.2 on 2022-11-21 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0005_rename_products_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_Name', models.CharField(blank=True, max_length=15, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Qty', models.IntegerField(blank=True, null=True)),
                ('Descr', models.CharField(blank=True, max_length=30, null=True)),
                ('P_Image', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('Category', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]