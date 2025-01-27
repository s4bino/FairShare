from django.contrib import admin
from django.urls import path, include  # Adicione o include aqui

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),  # Certifique-se de que essa linha está correta
]
