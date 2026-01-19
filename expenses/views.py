from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.db.models import Sum, F, Count, DecimalField
from django.core.paginator import Paginator

from .models import ExpenseItem, Ledger
from .forms import ExpenseItemForm, LedgerCreateForm

# Create your views here.


class LedgerListView(ListView):
    model = Ledger

    def get_queryset(self):
        return Ledger.objects.annotate(
            total_items=Count("items"),
            total_amt=Sum(
                F("items__qty") * F("items__price"),
                output_field=DecimalField(max_digits=12, decimal_places=2),
            ),  # double underscore is a lookup separator
        )


class LedgerDetailView(DetailView):
    model = Ledger
    context_object_name = "ledger"
    pk_url_kwarg = "ledger_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        raw_items = self.object.items.all().order_by("id")
        paginator = Paginator(raw_items, 5)
        page_number = self.request.GET.get("page")

        context["expenseitem_list"] = paginator.get_page(page_number)

        return context


class LedgerCreateView(CreateView):
    model = Ledger
    form_class = LedgerCreateForm

    def get_success_url(self):
        return reverse_lazy("expenses:ledgers")


class LedgerUpdateView(UpdateView):
    model = Ledger
    form_class = LedgerCreateForm
    pk_url_kwarg = "ledger_id"

    def get_success_url(self):
        return reverse_lazy(
            "expenses:ledger_detail", kwargs={"ledger_id": self.kwargs["ledger_id"]}
        )


class LedgerDeleteView(DeleteView):
    model = Ledger
    pk_url_kwarg = "ledger_id"

    def get_success_url(self):
        return reverse_lazy("expenses:ledgers")


class ExpenseListView(ListView):
    model = ExpenseItem
    template_name = "expenses/expenseitem_list.html"
    paginate_by = 5

    def get_queryset(self):
        return ExpenseItem.objects.filter(ledger_id=self.kwargs["ledger_id"]).order_by(
            "-id"
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["ledger"] = get_object_or_404(Ledger, id=self.kwargs["ledger_id"])
        return context


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
