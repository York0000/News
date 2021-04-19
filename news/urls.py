from django.urls import path

from news.views import NewsCreateView, NewsListView, NewsUpdateView, NewsDeleteView

app_name = 'news'

urlpatterns = [
    path('create/', NewsCreateView.as_view(), name='create'),
    path('update/<int:pk>/', NewsUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', NewsDeleteView.as_view(), name='delete'),
    path('', NewsListView.as_view(), name='list'),
]
