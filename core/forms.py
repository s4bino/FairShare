from django import forms
from core.models import Expense, Wallet
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'amount', 'wallet', 'beneficiaries']
        widgets = {
            'beneficiaries': forms.CheckboxSelectMultiple()
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar apenas carteiras onde o usuário é membro
        self.fields['wallet'].queryset = user.core_wallets.all()
        # Filtrar beneficiários apenas entre membros da carteira selecionada
        if 'wallet' in self.data:
            try:
                wallet_id = int(self.data.get('wallet'))
                wallet = Wallet.objects.get(id=wallet_id)
                self.fields['wallet'].queryset = user.core_wallets.all()
            except (ValueError, Wallet.DoesNotExist):
                pass
        elif self.instance.pk:
            User = get_user_model()
            self.fields['beneficiaries'].queryset = User.objects.all()

class AddMemberForm(forms.Form):
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )