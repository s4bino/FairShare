from django.contrib.auth.models import User
from django.db import models

class Wallet(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    members = models.ManyToManyField(User, related_name="core_wallets")

    def __str__(self):
        return self.name

class Expense(models.Model):
    wallet = models.ForeignKey(
        Wallet, 
        on_delete=models.CASCADE, 
        related_name="expenses"
    )
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    payer = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="paid_expenses"
    )
    beneficiaries = models.ManyToManyField(
        User, 
        related_name="shared_expenses"
    )

    def __str__(self):
        return f"{self.description} - {self.amount}"