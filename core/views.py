# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Expense
from .forms import ExpenseForm

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
            return redirect('expense_list')
    else:
        form = ExpenseForm(request.user)
    return render(request, 'core/add_expense.html', {'form': form})

@login_required
def expense_detail(request, pk):
    expense = get_object_or_404(Expense, pk=pk, wallet__members=request.user)
    return render(request, 'core/expense_detail.html', {'expense': expense})