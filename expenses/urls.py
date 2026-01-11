from django.urls import path
from .views import (
    Expenses,
    LedgerCreateView,
    Ledgers,
    LedgerDetailView,
    ExpenseCreateView,
)

app_name = "expenses"

urlpatterns = [
    path("", Expenses.as_view(), name="home"),
    path(
        "ledgers/<int:ledger_id>/items/add",
        ExpenseCreateView.as_view(),
        name="add_item",
    ),
    path("ledgers/", Ledgers.as_view(), name="ledgers"),
    path("ledgers/create/", LedgerCreateView.as_view(), name="ledger_create"),
    path("ledgers/<int:ledger_id>/", LedgerDetailView.as_view(), name="ledger_detail"),
]
