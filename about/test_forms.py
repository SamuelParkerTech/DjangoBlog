from django.test import TestCase
from .forms import CollaborateForm

"""
class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
    """    """ Test for all fields""" """
        form = CollaborateForm({
            'name': 'Samuel',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")


    def test_form_is_valid_name(self):
     """   """ Test for all fields""" """
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid NO NAME ENTERED")

    def test_form_is_valid_message(self):
    """   """ Test for all fields""" """
        form = CollaborateForm({
            'name': 'Samuel',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid NO MESSAGE ENTERED")

    def test_form_is_valid_email(self):
    """    """ Test for all fields""" """
        form = CollaborateForm({
            'name': 'Samuel',
            'email': '',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid NO EMAIL PROVIDED")

"""