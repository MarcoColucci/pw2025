
from django.urls import path
from .views import Inicio, SobreView, MapView
from .views import CountryCreate, EconomicBlockCreate, EconomicSectorCreate, BlockMembershipCreate, EconomyCreate
from .views import CountryDelete, EconomicBlockDelete, EconomicSectorDelete, BlockMembershipDelete, EconomyDelete
from .views import CountryUpdate, EconomicBlockUpdate, EconomicSectorUpdate, BlockMembershipUpdate, EconomyUpdate

from .views import CountryList

urlpatterns = [
    path("", Inicio.as_view(), name="inicio"),
    path("sobre/", SobreView.as_view(), name="sobre"),
    
    path("register/country", CountryCreate.as_view(), name="add-country"),
    path("register/economicbloc", EconomicBlockCreate.as_view(), name="add-economicbloc"),
    path("register/economicsector", EconomicSectorCreate.as_view(), name="add-economicsector"),
    path("register/blockmembership/", BlockMembershipCreate.as_view(), name="add-blockmembership"),
    path("register/economy/", EconomyCreate.as_view(), name="add-economy"),

# fazer delete, e update

    path("listar/pais/", CountryList.as_view(), name="Listar-Pais"),
]