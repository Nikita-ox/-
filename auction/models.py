from django.contrib.auth.models import User
from django.db import models as m


class PublishedManager(m.Manager):
    def get_queryset(self):
        return super().get_queryset() \
            .filter(status=Product.Status.PUBLISHED)


class Purchase(m.Model):
    customer = m.ForeignKey(User, on_delete=m.CASCADE, verbose_name="Кто купил")
    item = m.ForeignKey("Product", on_delete=m.CASCADE, verbose_name="Что купил")
    count = m.BooleanField()

    def __str__(self):
        return f'{self.customer} {self.item} {self.count}'

    class Meta:
        verbose_name = "Покупка"
        verbose_name_plural = "Покупки"


class Product(m.Model):
    class Status(m.TextChoices):
        DRAFT = "DR", "Draft"
        PUBLISHED = "PB", "Published"

    name = m.CharField(max_length=50, verbose_name="Имя")
    title = m.TextField(verbose_name="Описание")
    price = m.DecimalField(max_digits=19, decimal_places=2, verbose_name="Цена")
    status = m.CharField(
        max_length=2, choices=Status.choices,
        default=Status.DRAFT, verbose_name="Статус"
    )
    objects = m.Manager()
    published = PublishedManager()
    images = m.ImageField(verbose_name="Фото")

    def __str__(self):
        return f"{self.name} {self.price} {self.title} {self.images}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
