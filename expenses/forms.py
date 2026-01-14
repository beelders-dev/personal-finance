from django import forms
from .models import ExpenseItem, Ledger


class ExpenseItemForm(forms.ModelForm):
    class Meta:
        model = ExpenseItem
        fields = ["name", "qty", "price"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs.setdefault("placeholder", f"Enter {field.label.lower()}")


class LedgerCreateForm(forms.ModelForm):
    class Meta:
        model = Ledger
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs.setdefault("placeholder", f"Enter {field.label.lower()}")
