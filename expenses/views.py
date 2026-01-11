from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import ExpenseItem, Ledger

# Create your views here.


class Expenses(ListView):
    model = ExpenseItem


class Ledgers(ListView):
    model = Ledger


class LedgerDetailView(DetailView):
    model = Ledger
    template_name = "expenses/ledger_detail.html"
    context_object_name = "ledger"
    pk_url_kwarg = "ledger_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = self.object.items.all()

        return context


class LedgerCreateView(CreateView):
    model = Ledger
    fields = ["name"]


def get_success_url(self):
    return reverse_lazy("expenses:ledger_detail", kwargs={"ledger_id": self.object.id})


class ExpenseCreateView(CreateView):
    model = ExpenseItem
    fields = ["name", "qty", "price"]

    def form_valid(self, form):
        ledger = get_object_or_404(Ledger, id=self.kwargs["ledger_id"])
        form.instance.ledger = ledger
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ledger"] = get_object_or_404(Ledger, id=self.kwargs["ledger_id"])

        return context

    def get_success_url(self):
        return reverse_lazy(
            "expenses:ledger_detail", kwargs={"ledger_id": self.kwargs["ledger_id"]}
        )
