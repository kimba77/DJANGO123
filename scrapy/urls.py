from django.urls import path
from . import views, models

app_name = "scrapy_url"
urlpatterns = [
    path("parser", views.ParserFormView.as_view(), name="parser_view"),
    path("list/Watch", views.ParserListViewWatchs.as_view(), name="parser_Watchs"),
    path(
        "list/technodom",
        views.ParserListViewTechnodom.as_view(),
        name="parser_technodom",
    ),
]
