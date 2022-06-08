from django.db import models

# Create your models here.


class Bookshows(models.Model):
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    GENRE_CHOICE = (
        ("Fantazy", "Fantazy"),
        ("Detective", "Detective"),
        ("Humor", "Humor"),
        ("Roman", "Roman"),
        ("Adveture", "Adveture"),
        ("Science_fiction", "Science_fiction"),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to="", null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICE)
    tom = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Shows_user(models.Model):
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class ShowComment(models.Model):
    show = models.ForeignKey(
        Bookshows, on_delete=models.CASCADE, related_name="book_shows_comment"
    )
    user = models.ForeignKey(
        Shows_user, on_delete=models.CASCADE, related_name="shows_user", null=True
    )
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.show.title
