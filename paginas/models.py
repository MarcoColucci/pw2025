from django.db import models

# Todas as classes devem ter herança de models.Model

# Cria suas classes

# para objts - chaves extrangeira: (ForeignKey(referenciar qual é a classe, on_delete=models.PROTECT))

class Country(models.Model):
    # Definir atributos
    name = models.CharField(max_length=100)
    iso_code = models.CharField(max_length=2)

    def __str__(self):
        return f"Name: {self.name}"


class EconomicBloc(models.Model):
    name = models.CharField(max_length=100)


class CountryBlocMembership(models.Model):
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    bloc = models.ForeignKey(EconomicBloc, on_delete=models.PROTECT)  
    start = models.DateField()  
    end = models.DateField()  
    

class TradeData(models.Model):
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    year = models.PositiveSmallIntegerField(default=0)
    export_value = models.FloatField()
    import_value = models.FloatField()
    trade_balance = models.FloatField()
    gdp_share = models.FloatField()
    world_trade_share = models.FloatField()


class Kpi(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    value = models.FloatField()
    year = models.PositiveSmallIntegerField(default=0)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)