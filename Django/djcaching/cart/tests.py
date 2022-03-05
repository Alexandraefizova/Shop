from django.test import TestCase
import datetime
from django.utils import timezone
from cart.forms import CartAddProductForm


class CartAddProductFormTest(TestCase):

    def test_renew_form_date_field_label(self):
        form = CartAddProductForm()
        self.assertTrue(
            form.fields['quantity'].label is None)

    def test_renew_form_date_field_choices(self):
        form = CartAddProductForm()
        self.assertEqual(form.fields['quantity'].choices, [(i, str(i)) for i in range(1, 21)])

