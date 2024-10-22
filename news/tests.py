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

    # Test for saving a model object
    def test_save_method(self):
        self.mathew.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > o)
 
    # Test for deleting a model object
    def test_delete_method(self):
        self.mathew.save()
        self.mathew.delete()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) == 0)

    # Test for dislaying all saved objects
    def test_display_all_editors(self):
        editors = Editor.objects.all()
        self.assertIn(self.mathew, editors)

    # Test for updating a single object property
    def test_update_editor(self):
        self.mathew.save
        self.mathew.first_name = 'Matthew'
        self.mathew.save()
        updated_editor = Editor.objects.get(id=self.mathew.id)
        self.assertequal(updated_editor.first_name, 'Matthew')

class ArticleTestClass(TestCase):
    def setup(self):
        # Create an editor to use for this test
        self.mathew = Editor(first_name='Mathew', last_name='Orwa', email='okumuorwa@gmail.com')
        self.mathew.save()

        # Create a new article
        self.new_article = Article(title='Test Article', post='Test Post', editor=self.mathew)
        self.new_article.save()

        # Create a new tag
        self.new_tag = tag(name='Test Tag')
        self.new_tag.save()

        # Add the tag to the article
        self.new_article.tags.add(self.new_tag)

    #Test for saving a model object
    def test_save_article(self):
        self.new_article.save()
        article = Article.objects.all()
        self.assertTrue(len(articles) > 0)

    # Test for deleting a model object
    def test_delete_article(self):
        self.new_article.save()
        self.new_article.delete()
        articles =Article.objects.all()
        self.assertTrue(len(articles) == 0)

    # Test for displaying all saved objects
    def test_display_all_articles(self):
        self.new_article.save()
        articles = Article.objects.all()
        self.assertIn(self.new_article, articles)

    # Test To get Today's News
    def test_get_news_today(self):
        today_news = Article.today_news()
        self.asserTrue(len(today_news)>0)

    # test for updating a single object property
    def test_update_article(self):
        self.new_article.save()
        self.new_article.title = 'Updated Test Article'
        self.new_article.save()
        updated_article = Article.objects.get(id=self.new_article.id)
        self.assertEqual(updated_article.title, 'Updated Test Article')


class TagsTestClass(TestCase):
    def setUp(self):
        self.new_tag = tags(name= 'Test Tag')
        self.new_tag.save()

    # Test for saving a model object
    def test_save_tag(self):
        self.new_tag.save()
        tags_list = tags.objects.all()
        self.assertTrue(len(tags_list) > 0)

    # Test for deleting a object
    def test_delete_tag(self):
        self.new_tag.save()
        self.new_tag.delete()
        tags_list = tags.objects.all()
        self.assertTrue(len(tags_list) == 0)

    # test for displaying all saved objects
    def test_displaying_all_tags(self):
        self.new_tag.save()
        tags_list = tags.objects.all()
        self.assertIn(self.new_tag, tags_list)

    # test for updating a single object property
    def test_update_tag(self):
        self.new_tags.save()
        self.new_tag.name = 'Updated Tag'
        self.new_tag.save()
        updated_tag = tags.objects.get(id=self.new_tag.id) 
        self.assertEqual(updated_tag.name, 'Updated Tag')

        