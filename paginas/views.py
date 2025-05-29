from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# adicionado import abaixo
from django.db import models


from .models import Country, EconomicBlock, EconomicSector, BlockMembership, Economy

# CRIAR LINKS PARA NAVEGAÇÃO

# Função que converte o nome de uma URL na rota dela
from django.urls import reverse_lazy

class Inicio(TemplateView):
    template_name ="paginas/index.html"


class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'

# ---------------------- CREATE ----------------------

class CountryCreate(CreateView):
    template_name = "paginas/form.html"
    model = Country
    fields = ['name', 'iso_code']
    success_url = reverse_lazy('index')
    extra_context = {'title' : 'Register Country'}


class EconomicBlockCreate(CreateView):
    template_name = "paginas/form.html"
    model = EconomicBlock
    fields = ['name']
    success_url = reverse_lazy('index')
    extra_context = {'title' : 'Register Economic Bloc'}



class EconomicSectorCreate(CreateView):
    template_name = "paginas/form.html"
    model = EconomicSector
    fields = ['name']
    success_url = reverse_lazy('index')
    extra_context = {'title': 'Register Economic Sector'}



class BlockMembershipCreate(CreateView):
     country = models.ForeignKey(Country, on_delete=models.CASCADE)
     block = models.ForeignKey(EconomicBlock, on_delete=models.CASCADE)
     start_year = models.IntegerField()
     end_year = models.IntegerField(null=True, blank=True)

     def __str__(self):
         return f"{self.country.name} in {self.bloc.name} ({self.start_year} - {self.end_year or 'present'})"
    


class EconomyCreate(CreateView):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    year = models.IntegerField()
    export_value = models.FloatField()
    import_value = models.FloatField()
    sector = models.ForeignKey(EconomicSector, on_delete=models.CASCADE)

    def __str__(self):
        return f"Economic data for {self.country.name} - {self.year} - {self.sector.name}"


# ---------------------- UPDATEVIEW ----------------------

class CountryUpdate(UpdateView):
    template_name = "paginas/form.html"
    model = Country
    fields = ['name', 'iso_code']
    success_url = reverse_lazy('inicio')
    extra_context = {'title': 'Update Country'}


class EconomicBlockUpdate(UpdateView):
    template_name = "paginas/form.html"
    model = EconomicBlock
    fields = ['name']
    success_url = reverse_lazy('inicio')
    extra_context = {'title': 'Update Economic Bloc'}


class EconomicSectorUpdate(UpdateView):
    template_name = "paginas/form.html"
    model = EconomicSector
    fields = ['name']
    success_url = reverse_lazy('inicio')
    extra_context = {'title': 'Update Economic Sector'}


class BlockMembershipUpdate(UpdateView):
    template_name = "paginas/form.html"
    model = BlockMembership
    fields = ['country', 'block', 'start_year', 'end_year']
    success_url = reverse_lazy('inicio')
    extra_context = {'title': 'Update Block Membership'}


class EconomyUpdate(UpdateView):
    template_name = "paginas/form.html"
    model = Economy
    fields = ['country', 'year', 'export_value', 'import_value', 'sector']
    success_url = reverse_lazy('inicio')
    extra_context = {'title': 'Update Economic Data'}


# ---------------------- DELETEVIEW ----------------------

class CountryDelete(DeleteView):
    template_name = "paginas/form.html"
    model = Country
    success_url = reverse_lazy('inicio')
    extra_context = {'title': 'Delete Country'}


class EconomicBlockDelete(DeleteView):
    template_name = "paginas/form.html"
    model = EconomicBlock
    success_url = reverse_lazy('inicio')
    extra_context = {'title': 'Delete Economic Bloc'}


class EconomicSectorDelete(DeleteView):
    template_name = "paginas/form.html"
    model = EconomicSector
    success_url = reverse_lazy('inicio')
    extra_context = {'title': 'Delete Economic Sector'}


class BlockMembershipDelete(DeleteView):
    template_name = "paginas/form.html"
    model = BlockMembership
    success_url = reverse_lazy('inicio')
    extra_context = {'title': 'Delete Block Membership'}


class EconomyDelete(DeleteView):
    template_name = "paginas/form.html"
    model = Economy
    success_url = reverse_lazy('inicio')
    extra_context = {'title': 'Delete Economic Data'}
    
    
# ---------------------- ListView ----------------------

class CountryList(ListView):
    model = Country
    template_name ='paginas/country.html'
    