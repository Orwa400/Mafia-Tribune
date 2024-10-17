from django.test import TestCase
from .models import Editor,Article,tags

# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setup(self):
        self.mathew= editor(first_name = 'Mathew', last_name = 'Orwa', email = 'okumuorwa@gmail.com')

    # Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.mathew,Editor))

    def test_save_method(self):
        self.mathew.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > o)
        
