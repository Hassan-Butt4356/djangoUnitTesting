from django.test import SimpleTestCase

from myapp.forms import ItemCreateForm

class TestForms(SimpleTestCase):

    def test_item_form_no_data(self):
        form=ItemCreateForm({
            'title':'title',
            'price':4000,
            # 'detail':'some detail'
        })        
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),1)


    def test_item_form_data(self):
        form=ItemCreateForm({
            'title':'title',
            'price':4000,
            'detail':'some detail'
        })

        self.assertTrue(form.is_valid())