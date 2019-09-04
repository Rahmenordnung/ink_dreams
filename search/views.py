from django.shortcuts import render

# Create your views here.

def SearchFilters_BookView(request):
  return render(request, "searchFilter.html", )