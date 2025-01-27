from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('expenses/', views.expense_list, name='expense_list'),
    path('expenses/add/', views.add_expense, name='add_expense'),
    path('expenses/<int:pk>/', views.expense_detail, name='expense_detail'),
]