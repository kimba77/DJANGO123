from django.urls import path
from . import views, models
from datetime import datetime, timedelta

start_date = datetime.today() - timedelta(days=5)

app_name = "shows_url"
urlpatterns = [
    path("bookshow/", views.BookshowListViesw.as_view(), name="bookshow_all_url"),
    path(
        "bookshow/latest/",
        views.BookshowListViesw.as_view(
            queryset=models.Bookshows.objects.filter(
                created_date__gt=start_date
            ).order_by("-id")
        ),
        name="latest",
    ),
    path(
        "bookshow/Fantazy/",
        views.BookshowListViesw.as_view(
            queryset=models.Bookshows.objects.filter(genre="Fantazy").order_by("-id")
        ),
        name="Fantazy",
    ),
    path(
        "bookshow/Detective/",
        views.BookshowListViesw.as_view(
            queryset=models.Bookshows.objects.filter(genre="Detective").order_by("-id")
        ),
        name="Detective",
    ),
    path(
        "bookshow/Humor/",
        views.BookshowListViesw.as_view(
            queryset=models.Bookshows.objects.filter(genre="Humor").order_by("-id")
        ),
        name="Humor",
    ),
    path(
        "bookshow/Roman/",
        views.BookshowListViesw.as_view(
            queryset=models.Bookshows.objects.filter(genre="Roman").order_by("-id")
        ),
        name="Roman",
    ),
    path(
        "bookshow/Adveture/",
        views.BookshowListViesw.as_view(
            queryset=models.Bookshows.objects.filter(genre="Adveture").order_by("-id")
        ),
        name="Adveture",
    ),
    path(
        "bookshow/Science_fiction/",
        views.BookshowListViesw.as_view(
            queryset=models.Bookshows.objects.filter(genre="Science_fiction").order_by(
                "-id"
            )
        ),
        name="Science_fiction",
    ),
    path(
        "bookshow/<int:id>/", views.BookshowDetailView.as_view(), name="book_detail_url"
    ),
    path(
        "bookshow/<int:id>/update/", views.BookUpdateView.as_view(), name="book_update"
    ),
    path(
        "bookshow/<int:id>/delete/", views.BookDeleteView.as_view(), name="book_delete"
    ),
    path("add_book/", views.BookshowCreatedateView.as_view(), name="book_add"),
]
