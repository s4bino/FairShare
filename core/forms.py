from django import forms
from core.models import Expense
from core.models import Wallet

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
                self.fields['beneficiaries'].queryset = wallet.members.all()
            except (ValueError, Wallet.DoesNotExist):
                pass
        elif self.instance.pk:
            self.fields['beneficiaries'].queryset = self.instance.wallet.members.all()