from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    isbn = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
