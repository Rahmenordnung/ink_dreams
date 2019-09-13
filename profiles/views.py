from django.shortcuts import render
from book.models import Order

def profile_view(request):
  orders = Order.objects.filter(user=request.user, ordered=True)
  context = {
    'orders': orders
  }
  return render(request, "profile.html", context )
