from django.urls import reverse
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
# Create your models here.


class Book(models.Model):

    title = models.CharField(max_length=150)
    authors = models.ManyToManyField("Author", related_name="books")
    review = models.TextField(blank=True, null=True)		# can be empty
    reviewed_by = models.ForeignKey(User, blank=True, null=True, on_delete=True, related_name="reviews")
    date_reviewed = models.DateTimeField(blank=True, null=True)			# can be empty and true
    is_favourite = models.BooleanField(default=False, verbose_name="Favourite")		# setting default value

    def __str__(self):
        return "{} by{}".format(self.title, self.list_authors())

    def list_authors(self):
        return ", ".join([author.name for author in self.authors.all()])

    # over rides save
    def save(self, *args, **kwargs):
    
        if self.review and self.date_reviewed is None:
            self.date_reviewed = now()

        super(Book, self).save(*args, **kwargs)


class Author(models.Model):

    name = models.CharField(max_length=70, help_text="Use pen name, not real name",unique=True)

    def __str__(self):
        return "{}".format(self.name)
        # return "{} Author of {} book(s)".format(self.name, self.list_books())

    def list_books(self):
        published_books = len(self.books.all())
        # return published_books                  # returns number of books by particular author
        return ",".join([book.title for book in self.books.all()])     # returns title of books by author

    # old str func
    # def __str__(self):
        #  return self.name
    def get_absolute(self):
        return reverse('author-detail', kwargs={'pk',self.pk})
