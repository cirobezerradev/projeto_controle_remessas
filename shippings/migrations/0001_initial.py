# Generated by Django 5.1.2 on 2024-11-13 20:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('cliente', models.CharField(default=None, max_length=255)),
                ('nfe', models.IntegerField(primary_key=True, serialize=False)),
                ('data_emissao', models.DateField()),
                ('data_limite', models.DateField()),
                ('volumes', models.IntegerField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(default='PENDENTE', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingItem',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('codigo', models.IntegerField(default=None)),
                ('descricao', models.CharField(max_length=255)),
                ('un', models.CharField(max_length=6)),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nfe_remessa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shippings.shipping')),
            ],
            options={
                'unique_together': {('codigo', 'nfe_remessa')},
            },
        ),
        migrations.CreateModel(
            name='ShippingStorage',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('codigo', models.IntegerField(default=None)),
                ('descricao', models.CharField(max_length=255)),
                ('un', models.CharField(max_length=6)),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nfe_remessa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shippings.shipping')),
            ],
            options={
                'unique_together': {('codigo', 'nfe_remessa')},
            },
        ),
    ]
