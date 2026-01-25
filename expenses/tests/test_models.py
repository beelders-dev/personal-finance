from django.test import TestCase
from ..models import Ledger, ExpenseItem


class LedgerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.ledger = Ledger.objects.create(name="Supermarket")

    def test_ledger_str_name(self):
        """Test that the __str__ method returns the name."""
        self.assertEqual(str(self.ledger), "Supermarket")


class ExpenseItemTest(TestCase):

    # @classmethod
    # def setUpTestData(cls):
    #     cls.expense_item = ExpenseItem.objects.create(name="Banana", price=30, qty=12)

    def test_amt_calculates_correctly_for_positive_integers(self):
        """Test that the amt function returns the correct calculation."""
        item = ExpenseItem(price=30, qty=12)
        self.assertEqual(item.amt, 360)
