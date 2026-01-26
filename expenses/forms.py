from django import forms
from .models import ExpenseItem, Ledger


class BootstrapFormMixin:
    """A mixin to automatically add Bootstrap classes and placeholders."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs.setdefault("placeholder", f"Enter {field.label.lower()}")


class ExpenseItemForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = ExpenseItem
        fields = ["name", "qty", "price"]


class LedgerCreateForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Ledger
        fields = ["name"]
