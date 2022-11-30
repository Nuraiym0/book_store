from django.db import models

# Create your models here.


class Book(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published = models.DateTimeField()
    



# 3. создайте django проект с приложением book_store
# создайте модель book с полями category, title, price, published
