# from django.test import TestCase
# from .forms import CheckoutForm

# # Create your tests here.
# class CheckoutForm(TestCase):

#     def test_can_create_an_item_with_just_a_name(self):
#         form = CheckoutForm({'placeholder': '1234 Main St'})
#         self.assertTrue(form.is_valid())
    
#     def test_correct_message_for_missing_name(self):
#         form = CheckoutForm({'form': ''})
#         self.assertFalse(form.is_valid())
#         self.assertEqual(form.errors['name'], [u'This field is required.'])