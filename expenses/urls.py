from django.urls import path
from .views import (
    ExpenseHomeView,
    LedgerCreateView,
    Ledgers,
    LedgerDetailView,
    LedgerDeleteView,
    ExpenseCreateView,
    ExpenseUpdateView,
    ExpenseDeleteView,
)

app_name = "expenses"

urlpatterns = [
    path("", ExpenseHomeView.as_view(), name="home"),
    path(
        "ledgers/<int:ledger_id>/items/add",
        ExpenseCreateView.as_view(),
        name="add_item",
    ),
    path(
        "ledgers/<int:ledger_id>/items/<int:pk>/update",
        ExpenseUpdateView.as_view(),
        name="expense_update",
    ),
    path(
        "ledgers/<int:ledger_id>/items/<int:pk>/delete",
        ExpenseDeleteView.as_view(),
        name="expense_delete",
    ),
    path("ledgers/", Ledgers.as_view(), name="ledgers"),
    path("ledgers/create/", LedgerCreateView.as_view(), name="ledger_create"),
    path("ledgers/<int:ledger_id>/", LedgerDetailView.as_view(), name="ledger_detail"),
    path(
        "ledgers/<int:ledger_id>/delete",
        LedgerDeleteView.as_view(),
        name="ledger_delete",
    ),
]
