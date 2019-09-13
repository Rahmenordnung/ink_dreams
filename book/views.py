from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from .models import Book, OrderItem, Order, SaveCustomerAddress, Payment
from .forms import CheckoutForm
from django.utils import timezone

#Stripe Apy import

import stripe
stripe.api_key = settings.STRIPE_SECRET

# Book list class view that loading all products(books)

class BookDetailView(DetailView): 
    model = Book
    template_name = "book_detail.html"
    
# Add to cart method, checks if the object exists in the context or it creates it extracting it from the model, it filters it, and it saves the quantity added (one by one), or gives an error     
    
@login_required    
def add_book_to_cart(request, slug):
    item = get_object_or_404(Book, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )    
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        #chech if the book is already in the order 
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("book:order_final_view")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("book:order_final_view")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date) 
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
    return redirect("book:order_final_view")

# Remove from cart method, checks if the object withe an user assigned is the context, it filters it, if the object is there it removes it, or gives an error 

@login_required    
def remove_book_from_cart(request, slug):
    item = get_object_or_404(Book, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "This item was removed from your cart.")
            return redirect("book:order_final_view")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("book:book_detail", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("book:book_detail", slug=slug)
    
# Remove from cart method, checks if the object withe an user assigned is the context, it filters it, and if the quantity is more tha 0 it deletes one from the quantity in the context one by one, or gives an error    
    
@login_required 
def remove_one_book_from_cart(request, slug):
    item = get_object_or_404(Book, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
    # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if (order_item.quantity > 0):
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, "One book have been removed to your trolley")
            if order_item.quantity == 0:
                order.items.remove(order_item)
            return redirect("book:order_final_view")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("book:book_detail", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("book:book_detail", slug=slug)           
                


# Book list method for loading all products(books) for the search filters in the search app 
 
def products(request):
    context = {
        'items': Book.objects.all()
    }
    return render(request, "book_detail.html", context)

 # Check out product(book)

#  Get method :parsing the book as objects from the Book model through a context and rendering it in a check out Form, and if doesn´t exist giving an error

class CheckoutView(View):
    def get(self, *args, **kwargs):
        #form
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            form = CheckoutForm()
            context = {
                'form': form,
                'order': order}
            return render(self.request, "checkout.html", context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
            return redirect("book:checkout")
        
# Post method: Get the objects from the get method above and for each field save the data and if the data is correct continue to payment view, if not give an error           
    
    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                street_address = form.cleaned_data.get('street_address')
                house_address = form.cleaned_data.get('house_address')
                country = form.cleaned_data.get('country')
                zip = form.cleaned_data.get('zip')
                # TODO: add functionality for these fields
                # same_shipping_address = form.cleaned_data.get(
                #     'same_shipping_address')
                # save_info = form.cleaned_data.get('save_info')
                payment_option = form.cleaned_data.get('payment_option')
                billing_address = SaveCustomerAddress(
                    user=self.request.user,
                    street_address=street_address,
                    house_address=house_address,
                    country=country,
                    zip=zip
                )
                billing_address.save()
                order.billing_address = billing_address
                order.save()
                if payment_option == 'S':
                    return redirect('book:payment', payment_option='stripe')
                elif payment_option == 'P':
                    return redirect('book:payment', payment_option='paypal')
                else:
                    messages.warning(
                        self.request, "Invalid payment option selected")
                return redirect('book:checkout')
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("book:order-summary")
        
#Get the data , parse it into a context and obtain the stripe keys        

class PaymentView(View):
    def get(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        if order.billing_address:
            context = {
                'order': order,
                'stripe_publishable_key': settings.STRIPE_PUBLISHABLE 
            }
        else:
            messages.warning(self.request, "We don´t know where to send the order, please add a billing adress!")
            return redirect("book:checkout")
                
        return render(self.request, "payment.html", context)
    
# In this method the data saved is handeled with the help of Stripe script and key in order to process the virtual payment   

    def post(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        token = self.request.POST.get('stripeToken')
        amount = int(order.get_total() * 100)

        try:
            charge = stripe.Charge.create(
                amount=amount,  # eurocents
                currency="eur",
                source=token
            )

            # create the payment
            payment = Payment()
            payment.stripe_charge_id = charge['id']
            payment.user = self.request.user
            payment.amount = order.get_total()
            payment.save()

            # assign the payment to the order
            
            order_items = order.items.all()
            order_items.update(ordered=True)
            for item in order_items:
                item.save()

            order.ordered = True
            order.payment = payment
            order.save()

            messages.success(self.request, "Your order was successful!")
            return redirect("/")

        except stripe.error.CardError as e:
            body = e.json_body
            err = body.get('error', {})
            messages.warning(self.request, f"{err.get('message')}")
            return redirect("/")

        except stripe.error.RateLimitError as e:
            # Too many requests made to the API too quickly
            messages.warning(self.request, "Rate limit error")
            return redirect("/")

        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were supplied to Stripe's API
            messages.warning(self.request, "Invalid parameters")
            return redirect("/")

        except stripe.error.AuthenticationError as e:
            # Authentication with Stripe's API failed
            # (maybe you changed API keys recently)
            messages.warning(self.request, "Not authenticated")
            return redirect("/")

        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            messages.warning(self.request, "Network error")
            return redirect("/")

        except stripe.error.StripeError as e:
            # Display a very generic error to the user, and maybe send
            # yourself an email
            messages.warning(
                self.request, "Something went wrong. You were not charged. Please try again.")
            return redirect("/")

        except Exception as e:
            # send an email to ourselves
            messages.error(
                self.request, "A serious error occurred. We have been notifed.")
            return redirect("/")

# Book list method for loading all products

class HomeView(ListView):
    model = Book
    paginate_by = 10
    template_name = "home.html"
    
# Book list method for loading all products    
    
class OrderFinalView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'order_final_view.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("/")
    
# Book list method for loading all products

