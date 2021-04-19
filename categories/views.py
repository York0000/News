from django.urls import reverse
from django.views.generic import DeleteView, ListView, CreateView, UpdateView

from categories.forms import CategoryModelForm
from categories.models import CategoryModel


class CategoryCreateView(CreateView):
    template_name = 'form.html'
    form_class = CategoryModelForm

    def get_success_url(self):
        return reverse('categories:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create category'
        return context


class CategoryUpdateView(UpdateView):
    model = CategoryModel
    form_class = CategoryModelForm
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('categories:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update category'
        return context


class CategoriesListView(ListView):
    template_name = 'categories_list.html'
    model = CategoryModel


class CategoryDeleteView(DeleteView):
    model = CategoryModel

    def get_success_url(self):
        return reverse('categories:list')
