from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
    name = models.CharField(max_length=100)  # Nome da carteira
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # Saldo inicial
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='accounts_wallets'  # Nome único para evitar conflitos
    )

    def __str__(self):
        return f"{self.name} - {self.user.username}"
