# Generated by Django 5.1.2 on 2024-11-01 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shippings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingitem',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
