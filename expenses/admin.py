from django.contrib import admin

from .models import Ledger, ExpenseItem

# Register your models here.

admin.site.register(Ledger)
admin.site.register(ExpenseItem)
