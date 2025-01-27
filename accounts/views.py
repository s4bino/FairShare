from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import WalletForm 
from .models import Wallet


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/home.html'

@login_required
def add_wallet(request):
    if request.method == 'POST':
        form = WalletForm(request.POST)
        if form.is_valid():
            wallet = form.save(commit=False)
            wallet.user = request.user  # Relacionar ao usuário logado
            wallet.save()
            return redirect('home')  # Redirecionar após salvar
    else:
        form = WalletForm()
    return render(request, 'accounts/add_wallet.html', {'form': form})

def wallet_list(request):
    wallets = Wallet.objects.all()  # Obtém todas as carteiras do banco de dados
    return render(request, 'accounts/wallet_list.html', {'wallets': wallets})
