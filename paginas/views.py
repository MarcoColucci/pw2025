from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# adicionado import abaixo
from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Country, EconomicBlock, EconomicSector, BlockMembership, EconomicIndicator

# CRIAR LINKS PARA NAVEGAÇÃO

# Função que converte o nome de uma URL na rota dela
from django.urls import reverse_lazy

class Inicio(TemplateView):
    template_name ="paginas/map.html"


class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'
    
    
class MapView(TemplateView):
     template_name = 'paginas/map.html'

# ---------------------- CREATE ----------------------

class CountryCreate(LoginRequiredMixin, CreateView):
    model = Country
    template_name = "paginas/form.html"
    fields = ['name', 'gpd', 'hdi', 'population']
    success_url = reverse_lazy('country-list')
    extra_context = {'title': 'Register Country'}
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EconomicBlockCreate(LoginRequiredMixin, CreateView):
    model = EconomicBlock
    template_name = "paginas/form.html"
    fields = ['name']
    success_url = reverse_lazy('economicblock-list')
    extra_context = {'title': 'Register Economic Block'}
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BlockMembershipCreate(LoginRequiredMixin, CreateView):
    model = BlockMembership
    template_name = "paginas/form.html"
    fields = ['country', 'block', 'start_year', 'end_year']
    success_url = reverse_lazy('blockmembership-list')
    extra_context = {'title': 'Register Block Membership'}
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EconomicSectorCreate(LoginRequiredMixin, CreateView):
    model = EconomicSector
    template_name = "paginas/form.html"
    fields = ['name']
    success_url = reverse_lazy('economicsector-list')
    extra_context = {'title': 'Register Economic Sector'}
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EconomicIndicatorCreate(LoginRequiredMixin, CreateView):
    model = EconomicIndicator
    template_name = "paginas/form.html"
    fields = [
        'country', 'year', 'gdp', 'gdp_per_capita', 'population_total',
        'imports_goods_services', 'exports_goods_services', 'high_tech_exports'
    ]
    success_url = reverse_lazy('economicindicator-list')
    extra_context = {'title': 'Register Economic Indicator'}
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# ---------------------- UPDATE ----------------------

class CountryUpdate(LoginRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Country
    template_name = "paginas/form.html"
    fields = ['name', 'gpd', 'hdi', 'population']
    success_url = reverse_lazy('country-list')
    extra_context = {'title': 'Update Country'}
    def get_queryset(self):
        return Country.objects.filter(user=self.request.user)

class EconomicBlockUpdate(LoginRequiredMixin, UpdateView):
    model = EconomicBlock
    template_name = "paginas/form.html"
    fields = ['name']
    success_url = reverse_lazy('economicblock-list')
    extra_context = {'title': 'Update Economic Block'}
    def get_queryset(self):
        return Country.objects.filter(user=self.request.user)

class BlockMembershipUpdate(LoginRequiredMixin, UpdateView):
    model = BlockMembership
    template_name = "paginas/form.html"
    fields = ['country', 'block', 'start_year', 'end_year']
    success_url = reverse_lazy('blockmembership-list')
    extra_context = {'title': 'Update Block Membership'}
    def get_queryset(self):
        return Country.objects.filter(user=self.request.user)

class EconomicSectorUpdate(LoginRequiredMixin, UpdateView):
    model = EconomicSector
    template_name = "paginas/form.html"
    fields = ['name']
    success_url = reverse_lazy('economicsector-list')
    extra_context = {'title': 'Update Economic Sector'}
    def get_queryset(self):
        return Country.objects.filter(user=self.request.user)

class EconomicIndicatorUpdate(LoginRequiredMixin, UpdateView):
    model = EconomicIndicator
    template_name = "paginas/form.html"
    fields = [
        'country', 'year', 'gdp', 'gdp_per_capita', 'population_total',
        'imports_goods_services', 'exports_goods_services', 'high_tech_exports'
    ]
    success_url = reverse_lazy('economicindicator-list')
    extra_context = {'title': 'Update Economic Indicator'}

# ---------------------- DELETE ----------------------

class CountryDelete(DeleteView):
    model = Country
    template_name = "paginas/form.html"
    success_url = reverse_lazy('country-list')
    extra_context = {'title': 'Delete Country'}
    def get_queryset(self):
        return Country.objects.filter(user=self.request.user)

class EconomicBlockDelete(DeleteView):
    model = EconomicBlock
    template_name = "paginas/form.html"
    success_url = reverse_lazy('economicblock-list')
    extra_context = {'title': 'Delete Economic Block'}
    def get_queryset(self):
        return Country.objects.filter(user=self.request.user)

class BlockMembershipDelete(DeleteView):
    model = BlockMembership
    template_name = "paginas/form.html"
    success_url = reverse_lazy('blockmembership-list')
    extra_context = {'title': 'Delete Block Membership'}
    def get_queryset(self):
        return Country.objects.filter(user=self.request.user)

class EconomicSectorDelete(DeleteView):
    model = EconomicSector
    template_name = "paginas/form.html"
    success_url = reverse_lazy('economicsector-list')
    extra_context = {'title': 'Delete Economic Sector'}
    def get_queryset(self):
        return Country.objects.filter(user=self.request.user)

class EconomicIndicatorDelete(DeleteView):
    model = EconomicIndicator
    template_name = "paginas/form.html"
    success_url = reverse_lazy('economicindicator-list')
    extra_context = {'title': 'Delete Economic Indicator'}
    def get_queryset(self):
        return Country.objects.filter(user=self.request.user)

# ---------------------- LIST ----------------------

class CountryList(ListView):
    model = Country
    template_name = 'paginas/country_list.html'
    def get_queryset(self):
        return Country.objects.filter(user=self.request.user)

class EconomicBlockList(ListView):
    model = EconomicBlock
    template_name = 'paginas/economicblock_list.html'
    def get_queryset(self):
        return Country.objects.filter(user=self.request.user)

class BlockMembershipList(ListView):
    model = BlockMembership
    template_name = 'paginas/blockmembership_list.html'
    def get_queryset(self):
        return Country.objects.filter(user=self.request.user)
    

class EconomicSectorList(ListView):
    model = EconomicSector
    template_name = 'paginas/economicsector_list.html'
    def get_queryset(self):
        return Country.objects.filter(user=self.request.user)

class EconomicIndicatorList(ListView):
    model = EconomicIndicator
    template_name = 'paginas/economicindicator_list.html'
    def get_queryset(self):
        return Country.objects.filter(user=self.request.user)