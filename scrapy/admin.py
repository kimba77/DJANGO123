from django.contrib import admin
from . import models


class TechnodomAdmin(admin.ModelAdmin):
    # model =  models.Tehchnodom
    list_display = [
        "id",
        "image",
        "title",
        "price",
    ]

    list_filter = [
        "title",
    ]
    list_editable = [
        "title",
    ]
    search_fields = ["title"]


class WatchsAdmin(admin.ModelAdmin):
    # model =  models.Tehchnodom
    list_display = [
        "id",
        "link",
        "image",
        "title",
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


admin.site.register(models.Watchs, WatchsAdmin)

admin.site.register(models.Tehchnodom, TechnodomAdmin)
