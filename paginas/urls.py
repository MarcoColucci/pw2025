
from django.urls import path
from .views import Inicio, SobreView, MapView
from .views import CountryCreate, EconomicBlockCreate, EconomicSectorCreate, BlockMembershipCreate, EconomyCreate
from .views import CountryDelete, EconomicBlockDelete, EconomicSectorDelete, BlockMembershipDelete, EconomyDelete
from .views import CountryUpdate, EconomicBlockUpdate, EconomicSectorUpdate, BlockMembershipUpdate, EconomyUpdate
from django.contrib.auth import views as auth_views
from .views import CountryList

urlpatterns = [
    path("", Inicio.as_view(), name="inicio"),
    path("sobre/", SobreView.as_view(), name="sobre"),
    
    path("register/country", CountryCreate.as_view(), name="add-country"),
    path("register/economicbloc", EconomicBlockCreate.as_view(), name="add-economicbloc"),
    path("register/economicsector", EconomicSectorCreate.as_view(), name="add-economicsector"),
    path("register/blockmembership/", BlockMembershipCreate.as_view(), name="add-blockmembership"),
    path("register/economy/", EconomyCreate.as_view(), name="add-economy"),

    path('login/', auth_views.LoginView.as_view(template_name='paginas/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='paginas/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='paginas/password_change_done.html'), name='password_change_done'),

# fazer delete, e update

    path("listar/pais/", CountryList.as_view(), name="Listar-Pais"),
]