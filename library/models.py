# python manage.py makemigrations library (create the sql statement)
# python manage.py migrate (run the sql statments)

# python manage.py createsuperuser

from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=45)
    author = models.ForeignKey("Author", null=True, blank=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "books"

class Author(models.Model):
    name = models.CharField(max_length=45)
    age = models.IntegerField()
    contact_info = models.OneToOneField("ContactInfo", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "authors"

class ContactInfo(models.Model):
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.phone

    class Meta:
        db_table = "author_contact_info"

class List(models.Model):
    title = models.CharField(max_length=100)
    books = models.ManyToManyField("Book")

    def __str__(self):
        return self.title