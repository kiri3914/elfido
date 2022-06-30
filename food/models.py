
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    

class Food(models.Model):
    name = models.CharField(max_length=254)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    img = models.ImageField(upload_to='foods')
    desc = models.TextField()
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Table(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class BookTable(models.Model):
    name = models.CharField(max_length=255)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    date = models.DateTimeField()
    persons = models.IntegerField()
    message = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Клиент {self.name} заброни ровал столик {self.table.name}"


class Response(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    subjects = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    

class Event(models.Model):
    name = models.CharField(max_length=244)
    image = models.ImageField(upload_to='events')
    index = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    text1 = models.CharField(max_length=50)
    text2 = models.CharField(max_length=50)
    text3 = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self) -> str:
        return self.name




    







