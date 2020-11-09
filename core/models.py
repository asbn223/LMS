from django.db import models


class Books(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publish_date = models.DateField()

    def __str__(self):
        return self.book_name
