from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import generic
from django.urls import reverse
from . import models, forms


class ParserFormView(generic.FormView):
    template_name = "parser.html"
    form_class = forms.PerserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parse_data()
            return HttpResponse("Parsed data successfully")
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)


class ParserListViewWatchs(generic.ListView):
    template_name = "index.html"
    queryset = models.Watchs.objects.all()

    def get_queryset(self):
        return self.queryset


class ParserListViewTechnodom(generic.ListView):
    template_name = "technodom.html"
    queryset = models.Tehchnodom.objects.all()

    def get_queryset(self):
        return self.queryset
