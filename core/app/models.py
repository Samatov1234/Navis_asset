from django.db import models
from django_countries.fields import CountryField

class Partner(models.Model):
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

class Feedback(models.Model):
    name = models.CharField(verbose_name="Отзывы")
    user_name = models.CharField(max_length=250, verbose_name="Имя заказчика/покупателя")
    star = models.IntegerField(verbose_name="Звезда отзыва")
    text = models.TextField(verbose_name="Отзыв")
    date = models.DateField(verbose_name="Дата выхода отзывов")

    class Meta:
        verbose_name = "Отзывы"
        ordering = ['id']

class Application(models.Model):
    RECOVERY_CHOICES = (
        ('По приватному ключу','By private key'),
        ('Через файл Keystore + пароль','With Keystore file + password'),
        ('Через резервную копию','With backup'),
        ('С помощью сервиса поддержкиc', 'With the help of support service')
    )

    WALLET_TYPES = [
        ('hardware', 'Аппаратный'),
        ('software', 'Программный'),
        ('web', 'Онлайн'),
        ('mobile', 'Мобильный'),
        ('exchange', 'Биржевой'),
        ('paper', 'Бумажный'),
    ]

    name = models.CharField(max_length=250, verbose_name='Имя', default='Без имени')
    surname = models.CharField(max_length=250, verbose_name='Фамилия')
    country = CountryField(blank_label='Выберите страну')
    email = models.EmailField(default='test@example.com')
    phone = models.CharField(max_length=250)
    recovery_types = models.CharField(
        max_length=250,
        choices=RECOVERY_CHOICES,
        verbose_name='Тип восстановления'
    )
    wallet_type = models.CharField(
        max_length=20,
        choices=WALLET_TYPES,
        default='software',
        verbose_name='Тип кошелька'
    )
    wallet_volume = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Объем кошелька'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Application'
        ordering = ['id']