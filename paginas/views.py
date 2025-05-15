from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Country, EconomicBloc, CountryBlocMembership, TradeData,Kpi,HistoricalEvent,EconomicSector,SectorTradeData

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

    
class HistoricalEventCreate(CreateView):
    template_name = "paginas/form.html"
    model = HistoricalEvent
    fields = ['title', 'description', 'year']
    success_url = reverse_lazy('index')
    extra_context = {'title': 'Register Historical Event'}


class EconomicSectorCreate(CreateView):
    template_name = "paginas/form.html"
    model = EconomicSector
    fields = ['name']
    success_url = reverse_lazy('index')
    extra_context = {'title': 'Register Economic Sector'}


class SectorTradeDataCreate(CreateView):
    template_name = "paginas/form.html"
    model = SectorTradeData
    fields = ['name', 'country', 'sector', 'year', 'export_value', 'import_value']
    success_url = reverse_lazy('index')
    extra_context = {'title': 'Register Sector Trade Data'}
    # CRIAR LINKS PARA NAVEGAÇÃO
