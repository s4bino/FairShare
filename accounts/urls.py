from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.HomeView.as_view(), name='home'),
    path('add-wallet/', views.add_wallet, name='add_wallet'),  # Rota para adicionar carteira
    path('wallets/', views.wallet_list, name='wallet_list'),
]
