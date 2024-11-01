from django.db import models

class Shipping(models.Model):
    cliente = models.CharField(max_length=255)
    nfe = models.IntegerField(primary_key=True)
    data_emissao = models.DateField()
    volumes = models.IntegerField()
    peso = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.cliente}, {self.nfe}, {self.data_emissao}, {self.volumes}, {self.peso}'

class ShippingItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.IntegerField()
    descricao = models.CharField(max_length=255)
    un = models.CharField(max_length=6)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    valor_unit = models.DecimalField(max_digits=10, decimal_places=2)
    nfe_remessa = models.ForeignKey(Shipping, on_delete=models.CASCADE )

    def __str__(self) -> str:
        return f'{self.codigo}, {self.descricao}, {self.un}, {self.quantidade}, {self.valor_unit}'

class ShippingStorage(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.IntegerField()
    descricao = models.CharField(max_length=255)
    un = models.CharField(max_length=6)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    valor_unit = models.DecimalField(max_digits=10, decimal_places=2)
    nfe_remessa = models.ForeignKey(Shipping,on_delete=models.CASCADE )

    def __str__(self) -> str:
        return f'{self.codigo}, {self.descricao}, {self.un}, {self.quantidade}, {self.valor_unit}'
