from django.contrib import admin
from .models import Bookshows, ShowComment, Shows_user
from . import models


class BookshowAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "author",
        "genre",
    ]

    list_filter = [
        "title",
    ]
    list_editable = [
        "title",
    ]
    search_fields = [
        "title",
    ]


admin.site.register(models.Bookshows, BookshowAdmin)
