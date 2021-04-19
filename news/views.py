from django.db.models import Q
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from news.forms import NewsModelForm
from news.models import NewsModel


class NewsListView(ListView):
    template_name = 'news_list.html'

    def get_queryset(self):
        q = self.request.GET.get('q', '')

        return NewsModel.objects.filter(
            Q(title__icontains=q) |
            Q(author__name__icontains=q) |
            Q(category__title__icontains=q)
        )


class NewsCreateView(CreateView):
    template_name = 'form.html'
    form_class = NewsModel

    def get_success_url(self):
        return reverse('news:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create book'
        return context


class NewsUpdateView(UpdateView):
    model = NewsModel
    form_class = NewsModel
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('news:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update news'
        return context


class NewsDeleteView(DeleteView):
    model = NewsModel

    def get_success_url(self):
        return reverse('news:list')
