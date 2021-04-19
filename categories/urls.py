from django.urls import path

from categories.views import CategoryCreateView, CategoriesListView, CategoryUpdateView, CategoryDeleteView

app_name = 'categories'

urlpatterns = [
    path('', CategoriesListView.as_view(), name='list'),
    path('create/', CategoryCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CategoryUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CategoryDeleteView.as_view(), name='delete'),
]
