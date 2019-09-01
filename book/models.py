from django.conf import settings
from django.db import models
from django.shortcuts import reverse

GENGRE_ELECTION  = (
  ('FT','Fairy Tale'),
  ('BA','Biography/Autobiography'),
  ('CL','Classic'),
  ('RO','Romance'),
  ('AA','Action and Adventure'),
  ('CD','Crime and Detective'),
  ('CN','Comic and Graphic Novel'),
  ('HI','Historical Fiction'),
  ('MY','Mythology'),
  ('ST','Suspense/Thriller'),
  ('SF','Science Fiction'),
  ('F','Fantasy'),
  ('P','Poetry'),
  ('S','Satire'),
  ('E','Essay'),
)

STICKER_CHOICES = (
  ('P','primary'),
  ('S','secondary'),
  ('S','success'),
  ('D','danger'),
  ('W','warning'),
  ('I','info'),
  ('L','light'),
  ('D','dark')
)

class Book(models.Model):
    title = models.CharField(max_length=100)
    discount_price = models.FloatField(blank=True, null=True)
    price = models.FloatField()
    category = models.CharField(choices=GENGRE_ELECTION, max_length=2)
    sticker = models.CharField(choices=STICKER_CHOICES, max_length=2)
    slug= models.SlugField()
    description = models.TextField()

    def __str__(self):
        return self.title
      
    def get_absolute_url(self):
        return reverse("book:book_detail", kwargs={'slug': self.slug})
      
    def get_add_book_to_cart_url(self):
        return reverse("book:add_book_to_cart", kwargs={'slug': self.slug})
    
    def get_remove_book_from_cart(self):
        return reverse("book:remove_book_from_cart", kwargs={'slug': self.slug})    
      


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
    
    def get_total_item_price(self): 
        return self.quantity * self.item.price
    
    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price
    
    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total


