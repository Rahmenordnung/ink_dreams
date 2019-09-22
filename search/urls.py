from django.urls import path
from search.views import SearchFilters_BookView, search_function

app_name = 'search'

urlpatterns = [
  path('search/SearchFilters_BookView/', SearchFilters_BookView, name='Search'),
  path('', search_function, name='search')
]