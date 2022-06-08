from django.db import models


class Watchs(models.Model):
    class Meta:
        verbose_name = "Часы"
        verbose_name_plural = "Часы"

    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to="")
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.title


class Tehchnodom(models.Model):
    class Meta:
        verbose_name = "Техно дом"
        verbose_name_plural = "Техно дом"

    image = models.ImageField(upload_to="")
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField(max_length=100)

    def __str__(self):
        return self.title
