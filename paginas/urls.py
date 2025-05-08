
from django.urls import path
from .views import Inicio, SobreView
from .views import CountryCreate, EconomicBlocCreate, TradeDataCreate, KpiCreate

urlpatterns = [
    path("", Inicio.as_view(), name="inicio"),
    path("sobre/", SobreView.as_view(), name="sobre"),

    path("register/country", CountryCreate.as_view(), name="add-country"),
    path("register/economicbloc", EconomicBlocCreate.as_view(), name="add-economicbloc"),
    path("register/tradedata", TradeDataCreate.as_view(), name="add-tradedata"),
    path("register/kpi", KpiCreate.as_view(), name="add-kpi")
]  