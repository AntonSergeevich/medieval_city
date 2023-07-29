from django.db import models
from django.contrib.auth.models import User
from django import forms

class IndexPage(models.Model):
    name = models.CharField(blank=True,verbose_name='Имя')
    about_me = models.TextField(blank=True,verbose_name='Обо мне')
    work_experiens = models.TextField(blank=True,verbose_name='Опыт работы')
    projects = models.TextField(blank=True,verbose_name='Проекты')
    img = models.ImageField(blank=True, verbose_name='Фотография')
    class Meta:
        verbose_name_plural = 'Резюме'
    def __str__(self):
        return    f' {self.name}'
class MedieVallPage(models.Model):
    pass

class King(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Король')

    def __str__(self):
        return    f'Король'

class Person(models.Model):
    author = models.ForeignKey(King, on_delete=models.CASCADE)
    BOYARE = 'Боярин'
    DVORYANE = 'Дворянин'
    CATEGORY_CHOICES = (
        (BOYARE, 'Бояре'),
        (DVORYANE, 'Дворяне'),
    )
    categoryType = models.CharField(choices=CATEGORY_CHOICES, default=BOYARE, verbose_name='Категория')
    name = models.CharField(max_length=256, verbose_name='Имя Фамилия')
    year = models.CharField(max_length=256, verbose_name='Возраст')
    cash = models.CharField(max_length=256, verbose_name='Зарплата(золотых)')
    img = models.ImageField(blank=True, verbose_name='Изображение')

    def get_absolute_url(self):
        return f'/'

    class Meta:
        verbose_name_plural = 'Добавить Боярина или Дворянина'
    def __str__(self):
        return    f'{self.categoryType } {self.name}'
class Servant(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE ,verbose_name=f'Относится к:')
    name = models.CharField(max_length=256, verbose_name='Имя фамилия')
    year = models.CharField(max_length=256, verbose_name='Возраст')
    cash = models.CharField(max_length=256, verbose_name='Зарплата')

    def get_absolute_url(self):
        return f'/'

    class Meta:
        verbose_name_plural = 'Добавить Холопа'

    def __str__(self):
        return f'{self.name} | Относится к {self.author} {self.author.name}'