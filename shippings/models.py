from django.db import models

class Shipping(models.Model):
    nfe = models.IntegerField(primary_key=True)
    data_emissao = models.DateField()
    cliente = models.CharField(max_length=255)
    volumes = models.IntegerField()
    peso = models.DecimalField(max_digits=10, decimal_places=2)

class ShippingItem(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    codigo = models.IntegerField()
    descricao = models.CharField(max_length=255)
    un = models.CharField(max_length=6)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    valor_unit = models.DecimalField(max_digits=10, decimal_places=2)
    nfe_remessa = models.ForeignKey(Shipping, on_delete=models.CASCADE )

class ShippingStorage(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    codigo = models.IntegerField()
    descricao = models.CharField(max_length=255)
    un = models.CharField(max_length=6)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    valor_unit = models.DecimalField(max_digits=10, decimal_places=2)
    nfe_remessa = models.ForeignKey(Shipping,on_delete=models.CASCADE )






