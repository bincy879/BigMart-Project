# Generated by Django 4.1.2 on 2022-11-18 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0002_alter_products_email_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='User',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
