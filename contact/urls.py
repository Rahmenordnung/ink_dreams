from django.urls import path
from contact.views import ContactFormView

app_name = 'contact'

urlpatterns = [
  path('contact/ContactFormView/', ContactFormView, name='contact')
]