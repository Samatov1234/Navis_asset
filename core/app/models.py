from django.db import models


class Partners(models.Model):
    img = models.ImageField(verbose_name="Фото партнеров", upload_to="partners")
    class Meta:
        verbose_name = "Партнеры"
        ordering = ['id']

class FAQ(models.Model):
    question = models.CharField(max_length=250, verbose_name="Вопросы")
    answer = models.TextField(verbose_name="Ответы")

    class Meta:
        verbose_name = "Вопросы и ответы"
        ordering = ['id']


class News(models.Model):
    name = models.CharField(verbose_name="Новости")
    img = models.ImageField(verbose_name="Картина новости", upload_to="news")
    text = models.TextField(verbose_name="Описание")
    date = models.DateField(verbose_name="Дата выпуска")

    class Meta:
        verbose_name = "Новости"
        ordering = ['id']

class Review(models.Model):
    name = models.CharField(verbose_name="Отзывы")
    user_name = models.CharField(max_length=250, verbose_name="Имя заказчика/покупателя")
    star = models.IntegerField(verbose_name="Звезда отзыва")
    text = models.TextField(verbose_name="Отзыв")
    date = models.DateField(verbose_name="Дата выхода отзывов")

    class Meta:
        verbose_name = "Отзывы"
        ordering = ['id']

class Application(models.Model):
    first_name = models.CharField(verbose_name="Имя заявщика")
    last_name = models.CharField(verbose_name="Фамилия заявщика")
    country = models.CharField(verbose_name="Страна заявщика")
    e_mail = models.EmailField(verbose_name="E-mail заявщика")
    tel = models.IntegerField(verbose_name="Номер заявщика")

    class Meta:
        verbose_name = "Заявка"
        ordering = ['id']