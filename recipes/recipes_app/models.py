from django.db import models
from django.urls import reverse


soups = "Супы"
side_dishes = "Гарниры"
main_course = "Главное блюдо"
drinks = "Напитки"
snacks = "Закуски"
salads = "Салаты"

CATEGORIES = (
        (soups, "Супы"),
        (side_dishes, "Гарниры"),
        (main_course, "Главное блюдо"),
        (drinks, "Напитки"),
        (snacks, "Закуски"),
        (salads, "Салаты")
)


class Category(models.Model):
     name = models.CharField(max_length=50)

     def __str__(self):
         return self.name

class Dish(models.Model):
     name = models.CharField(max_length=255)
     photo = models.ImageField(upload_to='images/', default=None)
     category = models.ForeignKey(Category, on_delete=models.CASCADE)
     description = models.TextField()

     def __str__(self):
         return f'{self.name}'


class Step(models.Model):
     description = models.TextField()
     dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
     order = models.IntegerField()
     photo = models.ImageField(upload_to='images/', default=None)

     def __str__(self):
         return f'{self.description} ({self.dish})'
