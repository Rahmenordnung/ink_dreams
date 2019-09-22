from django.db.models import Q
from django.shortcuts import render
from book.models import Book, GENGRE_ELECTION


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = Book.objects.all()
    title_contains_query = request.GET.get('title_contains')
    title_or_work_price_query = request.GET.get('title_or_work_price_query')
    title_or_author_query = request.GET.get('author_or_title')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    bestseller = request.GET.get('bestseller')
    not_bestseller = request.GET.get('notbestseller')
    is_longbook = request.GET.get('longbook')
    is_shortbook = request.GET.get('isshortbook')
    worldwide_appreciated = request.GET.get('worldwide_appreciated')
    underground_appreciation = request.GET.get('underground_appreciation')
    category = request.GET.get('category')

    if is_valid_queryparam(title_contains_query):
            qs = qs.filter(title__icontains=title_contains_query)
    elif is_valid_queryparam(title_or_work_price_query):
            qs = qs.filter(Q(title__icontains=title_or_work_price_query)
                        | Q(price__iexact=title_or_work_price_query)
                        ).distinct()            
      
    elif is_valid_queryparam(title_or_author_query):
            qs = qs.filter(Q(title__icontains=title_or_author_query)
                        | Q(work_author__icontains=title_or_author_query)
                        ).distinct()

    if is_valid_queryparam(date_min):
        qs = qs.filter(publish_date__gte=date_min)

    if is_valid_queryparam(date_max):
        qs = qs.filter(publish_date__lt=date_max)

    if bestseller == 'on':
        qs = qs.filter(bestseller=True)
    elif not_bestseller == 'on':
        qs = qs.filter(bestseller=False)
        
    if is_longbook == 'on':
        qs = qs.filter(longbook=True)
    elif is_shortbook == 'on':
        qs = qs.filter(longbook=False)

    if worldwide_appreciated == 'on':
        qs = qs.filter(worldwide_appreciated=True)
    elif underground_appreciation == 'on':
        qs = qs.filter(worldwide_appreciated=False)

    if is_valid_queryparam(category) and category != 'Choose...':
        qs = qs.filter(category=category)

    return qs


def SearchFilters_BookView(request):
    qs = filter(request)
    context = {
        'queryset': qs,
        'categories': GENGRE_ELECTION
    }
    return render(request, "searchFilter.html", context)

def search_function(request):
  literature_work = Book.objects.filter(title__icontains=request.GET['q'])
  return render(request, "home.html", {"literature_work":literature_work})