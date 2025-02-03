from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('expenses/', views.expense_list, name='expense_list'),
    path('expenses/add/', views.add_expense, name='add_expense'),
    path('expenses/<int:pk>/', views.expense_detail, name='expense_detail'),
    path('wallets/', views.wallet_list, name='wallet_list'),
    path('wallets/add/', views.add_wallet, name='add_wallet'),
    path('wallets/<int:wallet_id>/', views.wallet_detail, name='wallet_detail'),
    path('wallets/<int:wallet_id>/add-members/', views.add_members, name='add_members'),
]