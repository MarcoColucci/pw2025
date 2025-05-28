from django.db import models

# Todas as classes devem ter herança de models.Model

# Cria suas classes

# para objts - chaves extrangeira: (ForeignKey(referenciar qual é a classe, on_delete=models.PROTECT))

class Country(models.Model):
    # Definir atributos
    # gpd = pib
    # hdi = idh

    name = models.CharField(max_length=100)
    gpd = models.CharField(max_length=100)
    hdi = models.CharField(max_length=100)
    population = models.CharField(max_length=100)

    def __str__(self):
        return f"Name: {self.name}"


class EconomicBlock(models.Model):
    name = models.CharField(max_length=100)


class BlockMembership(models.Model):
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    block = models.ForeignKey(EconomicBlock, on_delete=models.PROTECT)  
    start_year= models.DateField()  
    end_year = models.DateField()  
    
class EconomicSector(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Economy(models.Model):
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    year = models.IntegerField()
    export_value = models.FloatField()
    import_value = models.FloatField()
    sector = models.ForeignKey(EconomicSector, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.country.name} - {self.year} - {self.sector.name}"