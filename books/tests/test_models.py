from django.test import TestCase
from books.models import Book
from books.factories import AuthorFactory
# Create your tests here.


'''class DemoTest(TestCase):
    def test_addition(self):
        self.assertEqual(1+1,3)'''


# Create your test here,
class BookTest(TestCase):
    def setUp(self):
        self.author1 = AuthorFactory(name="Author 1")
        self.author2 = AuthorFactory(name="Author 2")

        self.book = Book(title="MyBook")
        self.book.save()
        self.book.authors.add(self.author1.pk, self.author2.pk)

    def tearDown(self):
        self.author1.delete()
        self.author2.delete()
        self.book.delete()

    def test_can_list_authors(self):
        self.assertEqual("Author 1, Author 2", self.book.list_authors())

    def test_custom_save_method(self):
        self.assertIsNone(self.book.date_reviewed)
        self.book.review = "MyReview"
        self.book.save()
        self.assertIsNotNone(self.book.date_reviewed)