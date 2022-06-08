from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from . import models, forms
import scrapy
from datetime import datetime, timedelta
from django.views import generic

start_date = datetime.today() - timedelta(days=5)


class BookshowListViesw(generic.ListView):
    template_name = "bookshow.html"
    queryset = models.Bookshows.objects.order_by("-id")

    def get_queryset(self):
        return self.queryset


# def bookshow(request):
#     queryset = models.Bookshows.objects.order_by("id")
#     return render(request,"bookshow.html",{"shows":queryset})


class BookshowDetailView(generic.DetailView):
    template_name = "book_detail.html"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get("id")
        return get_object_or_404(models.Bookshows, id=show_id)


# def book_show_detail(request,id):
#     object = get_object_or_404(models.Bookshows,id=id)
#     return render(request,"book_detail.html",{"show":object})


class BookshowCreatedateView(generic.CreateView):
    template_name = "add_shows.html"
    form_class = forms.Form_for_bookshow
    queryset = models.Bookshows.objects.all()
    success_url = "/bookshow/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookshowCreatedateView, self).form_valid(form=form)


# def add_book_user(request):
#     method = request.method
#     if method == "POST":
#         form = forms.Form_for_bookshow(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # return HttpResponse("TVShow Created successfully")
#             return redirect(reverse("shows_url:bookshow_all_url"))
#     else:
#         form = forms.Form_for_bookshow()
#     return render(request, "add_shows.html", {"form": form})


class BookUpdateView(generic.UpdateView):
    template_name = "book_update.html"
    form_class = forms.Form_for_bookshow
    success_url = "/bookshows/"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get("id")
        return get_object_or_404(models.Bookshows, id=show_id)

    def form_valid(self, form):
        print(form.cleaned_data)


# def book_update(request,id):
#     book_object = get_object_or_404(models.Bookshows,id = id)
#     if request.method == "POST":
#         form = forms.Form_for_bookshow(instance=book_object,data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("shows_url:bookshow_all_url"))
#     else:
#         form = forms.Form_for_bookshow(instance=book_object)
#     return render(request,"book_update.html",{"form":form,
#                                                 "object":book_object})


class BookDeleteView(generic.DeleteView):
    success_url = "/bookshow/"
    template_name = "confirm_delete_book.html"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get("id")
        return get_object_or_404(models.Bookshows, id=show_id)


# def book_delete(request, id):
#     book_object = get_object_or_404(models.Bookshows, id=id)
#     book_object.delete()
#     return redirect(reverse("shows_url:bookshow_all_url"))


# def books_latest(request):
#     queryset = models.Bookshows.objects.filter(created_date__gt=start_date).order_by("-id")
#     return render(request, "bookshow.html", {"shows": queryset})
#
#
# def books_Fantazy(request):
#     main = models.Bookshows.objects.filter(genre="Fantazy").order_by("-id")
#     return render(request,"bookshow.html",{"shows":main})
#
# def books_Detective(request):
#     queryset = models.Bookshows.objects.filter(genre="Detective").order_by("-id")
#     return render(request,"bookshow.html",{"show":queryset})
#
# def books_Humor(request):
#     queryset = models.Bookshows.objects.filter(genre="Humor").order_by("-id")
#     return render(request,"bookshow.html",{"show":queryset})
#
# def books_Roman(request):
#     queryset = models.Bookshows.objects.filter(genre="Roman").order_by("-id")
#     return render(request,"bookshow.html",{"shows":queryset})
#
# def books_Adveture(request):
#     queryset = models.Bookshows.objects.filter(genre="Adveture").order_by("-id")
#     return render(request,"bookshow.html",{"shows":queryset})
#
#
# def books_Science_fiction(request):
#     queryset = models.Bookshows.objects.filter(genre="Science_fiction").order_by("-id")
#     return render(request,"bookshow.html",{"shows":queryset})
