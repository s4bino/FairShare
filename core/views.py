from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Expense, Wallet
from .forms import ExpenseForm
from .forms import AddMemberForm

# EXPENSES FUNCS

@login_required
def expense_list(request):
    # Listar despesas das carteiras onde o usuário é membro
    expenses = Expense.objects.filter(wallet__members=request.user)
    return render(request, 'core/expense_list.html', {'expenses': expenses})

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.user, request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.payer = request.user
            expense.save()
            form.save_m2m()  # Salvar relações many-to-many
            messages.success(request, 'Despesa adicionada com sucesso!')
            return redirect('core:expense_list')
    else:
        form = ExpenseForm(request.user)
    return render(request, 'core/add_expense.html', {'form': form})

@login_required
def expense_detail(request, pk):
    expense = get_object_or_404(Expense, pk=pk, wallet__members=request.user)
    return render(request, 'core/expense_detail.html', {'expense': expense})

# WALLET FUNCS

@login_required
def wallet_list(request):
    wallets = Wallet.objects.filter(members=request.user)
    return render(request, 'core/wallet_list.html', {'wallets': wallets})

@login_required
def add_wallet(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        balance = request.POST.get('balance', 0)
        wallet = Wallet.objects.create(
            name=name,
            description=description,
            balance=balance
        )
        wallet.members.add(request.user)
        messages.success(request, 'Carteira criada com sucesso!', extra_tags='wallet')
        return redirect('core:wallet_list')
    return render(request, 'core/add_wallet.html')

@login_required
def wallet_detail(request, wallet_id):
    # Recupera a carteira ou retorna um erro 404 se não existir
    wallet = get_object_or_404(Wallet, id=wallet_id, members=request.user)
    return render(request, 'core/wallet_detail.html', {'wallet': wallet})

@login_required
def add_members(request, wallet_id):
    wallet = get_object_or_404(Wallet, id=wallet_id, members=request.user)  # Apenas membros da carteira podem adicionar outros
    if request.method == 'POST':
        form = AddMemberForm(request.POST)
        if form.is_valid():
            users = form.cleaned_data['users']
            wallet.members.add(*users)  # Adiciona os usuários selecionados à carteira
            messages.success(request, 'Membros adicionados com sucesso!')
            return redirect('core:wallet_detail', wallet_id=wallet.id)
    else:
        form = AddMemberForm()
    return render(request, 'core/add_members.html', {'form': form, 'wallet': wallet})