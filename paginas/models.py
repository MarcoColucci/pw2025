from django.db import models
from django.contrib.auth.models import User
# Todas as classes devem ter herança de models.Model

# Cria suas classes

# para objts - chaves extrangeira: (ForeignKey(referenciar qual é a classe, on_delete=models.PROTECT))

class Country(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="countries")
    name = models.CharField(max_length=100)
    gpd = models.CharField(max_length=100)
    hdi = models.CharField(max_length=100)
    population = models.CharField(max_length=100)

    def __str__(self):
        return f"Name: {self.name}"


class EconomicBlock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="economic_blocks")
    name = models.CharField(max_length=100)


class BlockMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="block_memberships")
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    block = models.ForeignKey(EconomicBlock, on_delete=models.PROTECT)  
    start_year= models.DateField()  
    end_year = models.DateField()  


class EconomicSector(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="economic_sectors")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 🔹 Nova tabela para armazenar indicadores econômicos
class EconomicIndicator(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="ecomic_indicators")
    year = models.IntegerField()

    gdp = models.FloatField(help_text="PIB total em dólares")
    gdp_per_capita = models.FloatField(help_text="PIB per capita em dólares")
    population_total = models.BigIntegerField(help_text="População total")
    imports_goods_services = models.FloatField(help_text="Importações de bens e serviços (% do PIB)")
    exports_goods_services = models.FloatField(help_text="Exportações de bens e serviços (% do PIB)")
    high_tech_exports = models.FloatField(help_text="Exportações de alta tecnologia (% das exportações manufatureiras)")

    def __str__(self):
        return f"{self.country.name} - {self.year}"