from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Country, EconomicBloc, CountryBlocMembership, TradeData,Kpi

# Função que converte o nome de uma URL na rota dela
from django.urls import reverse_lazy

class Inicio(TemplateView):
    template_name ="paginas/index.html"


class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'


class CountryCreate(CreateView):
    template_name = "paginas/form.html"
    model = Country
    fields = ['name', 'iso_code']
    success_url = reverse_lazy('index')
    extra_context = {'title' : 'Register Country'}


class EconomicBlocCreate(CreateView):
    template_name = "paginas/form.html"
    model = EconomicBloc
    fields = ['name']
    success_url = reverse_lazy('index')
    extra_context = {'title' : 'Register Economic Bloc'}


class TradeDataCreate(CreateView):
    template_name = "paginas/form.html"
    model = TradeData
    fields = ['country', 'year', 'export_value', 'import_value', 'trade_balance', 'gdp_share', 'world_trade_share']
    success_url = reverse_lazy('index')
    extra_context = {'title' : 'Register Trade Data'}


class KpiCreate(CreateView):
    template_name = "paginas/form.html"
    model = Kpi
    fields = ['name', 'description', 'value', 'country']
    success_url = reverse_lazy('index')
    extra_context = {'title' : 'Register Kpi'}

    # CRIAR LINKS PARA NAVEGAÇÃO
