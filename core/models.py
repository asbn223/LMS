import os
import uuid

from django.db import models


def recipe_image_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/book/', filename)


class Books(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publish_date = models.DateField()
    desc = models.TextField(null=True)
    img = models.ImageField(upload_to=recipe_image_file_path, null=True)

    def __str__(self):
        return self.book_name
