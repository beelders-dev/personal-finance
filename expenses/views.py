from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import ExpenseItem, Ledger
from .forms import ExpenseItemForm

# Create your views here.


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
        return reverse_lazy("expenses:ledgers")


class ExpenseHomeView(ListView):
    model = ExpenseItem
    template_name = "expenses/expenses_home.html"


class ExpenseCreateView(CreateView):
    model = ExpenseItem
    form_class = ExpenseItemForm

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


class ExpenseUpdateView(UpdateView):
    model = ExpenseItem
    form_class = ExpenseItemForm

    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ledger"] = get_object_or_404(Ledger, id=self.kwargs["ledger_id"])
        return context

    def get_success_url(self):
        return reverse_lazy(
            "expenses:ledger_detail", kwargs={"ledger_id": self.kwargs["ledger_id"]}
        )


class ExpenseDeleteView(DeleteView):
    model = ExpenseItem
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ledger"] = get_object_or_404(Ledger, id=self.kwargs["ledger_id"])
        return context

    def get_success_url(self):
        return reverse_lazy(
            "expenses:ledger_detail", kwargs={"ledger_id": self.kwargs["ledger_id"]}
        )
