from django.test import TestCase
from ..models import Ledger, ExpenseItem


class LedgerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.ledger = Ledger.objects.create(name="Supermarket")

    def test_ledger_str_name(self):
        """Test that the __str__ method returns the name."""
        self.assertEqual(str(self.ledger), "Supermarket")


# class ExpenseItemTest(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         cls.expense_item = ExpenseItem.objects.create(
#             name="Banana", qty="12", price="50.00"
#         )

#     def test_
