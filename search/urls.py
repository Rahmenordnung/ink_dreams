from django.urls import path
from search.views import SearchFilters_BookView

app_name = 'search'

urlpatterns = [
  path('search/SearchFilters_BookView/', SearchFilters_BookView, name='Search')
]