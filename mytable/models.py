from django.db import models

class MyTable(models.Model):
    name = models.CharField(max_length=255)  # Поле для имени
    age = models.IntegerField()  # Поле для возраста

    def __str__(self):
        return self.name
