from django.test import TestCase
from ..models import Ledger, ExpenseItem
from django.core.exceptions import ValidationError


class LedgerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.ledger = Ledger.objects.create(name="Supermarket")

    def test_ledger_str_name_displays_correctly(self):
        """Test that the __str__ method returns the name."""
        self.assertEqual(str(self.ledger), "Supermarket")


class ExpenseItemTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.ledger = Ledger.objects.create(name="Groceries")
        cls.expense_item = ExpenseItem.objects.create(
            ledger=cls.ledger, name="Banana", qty=12, price=30
        )

    def test_expenseitem_str_name_displays_correctly(self):
        """Test that the __str__ method returns the name"""
        self.assertEqual(str(self.expense_item), "Banana")

    def test_amt_calculates_correctly_for_positive_integers(self):
        """Test that the amt function returns the correct product."""
        item = ExpenseItem(price=30, qty=12)
        self.assertEqual(item.amt, 360)

    def test_amt_calculates_correctly_with_decimal_price(self):
        """Test that amt handles decimal prices like 10.50."""
        item = ExpenseItem(price=10.50, qty=2)
        self.assertEqual(item.amt, 21.00)

    def test_amt_returns_zero_if_qty_is_zero(self):
        """Test that the amt function returns zero if the qty is zero."""
        item = ExpenseItem(price=15, qty=0)
        result = item.amt
        self.assertEqual(result, 0)

    def test_amt_returns_zero_if_price_is_zero(self):
        """Test that the amt function returns zero if the price is zero."""
        item = ExpenseItem(price=0, qty=12)
        result = item.amt
        self.assertEqual(result, 0)

    def test_negative_qty_raises_validation_error(self):
        """Test that ExpenseItem will not be created with a negative qty."""
        item = ExpenseItem(ledger=self.ledger, name="Apple", qty=-50, price=20)

        with self.assertRaises(ValidationError):
            item.full_clean()

    def test_negative_price_raises_validation_error(self):
        """Test that ExpenseItem will not be created with a negative price."""
        item = ExpenseItem(ledger=self.ledger, name="Apple", qty=50, price=-20)

        with self.assertRaises(ValidationError):
            item.full_clean()

    def test_expenseitem_belongs_to_the_correct_ledger(self):
        """Test that the expense item is linked to the ledger."""
        item = ExpenseItem.objects.create(
            ledger=self.ledger, name="Apple", qty=12, price=30
        )

        self.assertEqual(item.ledger, self.ledger)
        self.assertEqual(item.ledger.name, "Groceries")

    def test_ledger_can_access_its_items_backwards(self):
        """Test that the ledger can see all its linked ExpenseItems."""
        items = self.ledger.items.all()

        self.assertIn(self.expense_item, items)
        self.assertEqual(items.count(), 1)
