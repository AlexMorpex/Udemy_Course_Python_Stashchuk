from django.db import models
from django.utils import timezone
# Создаём модель для табличек ( модель (класс) это описание таблицы какой она будет)

# Делаем так, что в каждой записи в таблице Category будут колонки
# которые указаны ниже: title, created_at. Каждый параметр класса( таблички ) это одна колонка


class Category(models.Model):  # табличка 1
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(
        default=timezone.now)  # Дата генерится автоматически

    def __str__(self):
        return self.title


class Course(models.Model):  # табличка 2
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    students_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    created_at = models.DateTimeField(
        default=timezone.now)  # Дата генерится автоматически

    def __str__(self):
        return self.title
