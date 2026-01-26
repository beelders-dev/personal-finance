from django.test import TestCase
from ..forms import ExpenseItemForm
from ..models import Ledger


class ExpenseItemFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.ledger = Ledger.objects.create(name="Expenses List")

    def test_form_is_valid_with_good_data(self):
        """Test that the form accepts valid input."""
        data = {"name": "Carrot", "qty": 5, "price": 12}
        form = ExpenseItemForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_is_invalid_without_name(self):
        """Test that name is required."""
        data = {"qty": 5, "price": 12}
        form = ExpenseItemForm(data=data)
        self.assertFalse(form.is_valid())

        self.assertIn("name", form.errors)

    def test_form_is_invalid_without_qty(self):
        """Test that qty is required."""
        data = {"name": "Carrot", "price": 12}
        form = ExpenseItemForm(data=data)
        self.assertFalse(form.is_valid())

        self.assertIn("qty", form.errors)

    def test_form_is_invalid_without_price(self):
        """Test that price is required."""
        data = {"name": "Carrot", "qty": 5}
        form = ExpenseItemForm(data=data)
        self.assertFalse(form.is_valid())

        self.assertIn("price", form.errors)

    def test_form_has_bootstrap_classes_and_placeholders(self):
        """Verify the custom __init__ logic is working."""
        form = ExpenseItemForm()
        # Check 'name' as a representative of the loop
        self.assertEqual(form.fields["name"].widget.attrs["class"], "form-control")
        self.assertEqual(form.fields["name"].widget.attrs["placeholder"], "Enter name")
