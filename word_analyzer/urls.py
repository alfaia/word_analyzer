from django.urls import path
from .views import VowelCountView, SortView


urlpatterns = [
    path('vowel_count/', VowelCountView.as_view(), name='vowel-count'),
    path('sort/', SortView.as_view(), name='sort-words'),
]
