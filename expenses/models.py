from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Ledger(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField

    def __str__(self):
        return self.name


class ExpenseItem(models.Model):
    ledger = models.ForeignKey(Ledger, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=100)
    qty = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return self.qty * self.price

    def __str__(self):
        return self.name
