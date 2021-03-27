from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Category, Setting


class MainIndex(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):

        kwargs['phone'] = Setting.objects.get(key='phone').value
        return super().get_context_data(**kwargs)


class MainCategory(TemplateView):
    template_name = "main/category.html"

    def get_context_data(self, **kwargs):

        kwargs['phone'] = Setting.objects.get(key='phone').value
        return super().get_context_data(**kwargs)