import datetime
import random
from django.core.management.base import BaseCommand
from book.models import Book, Author, Category

categories = [
  'Fairy Tale',
  'Biography/Autobiography',
  'Classic',
  'Romance',
  'Action and Adventure',
  'Crime and Detective',
  'Comic and Graphic Novel',
  'Historical Fiction',
  'Mythology',
  'Suspense/Thriller',
  'Science Fiction',
  'Fantasy',
  'Poetry',
  'Satire',
  'Essay'
]

authors = ['Homer', 'Kafka','Cervantes', 'Moliere', 'Poe', 'Dante', 'Goethe', 'Shakespeare', 'Marquez', 'Confucius' ]

def generate_author_name():
  index = random.randint(0, 9)
  return authors[index]

def generate_category_name():
  index = random.randint(0, 14)
  return categories[index]

def generate_discount_price_count():
  return random.randint(0, 100)
  
def generate_price_count():
  return random.randint(0, 500)

def generate_publish_date():
    year = random.randint(30, 2030)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return datetime.date(year, month, day)
  
class Command(BaseCommand):
  
  def add_arguments(self, parser):
    parser.add_argument(
      'file_name', type=str, help='A list of the available random books')
    
  def handle(self, *args, **kwargs):
    file_name = kwargs['file_name']
    with open (f'{file_name}.txt') as file:
      for row in file:
        title = row
        author_name = generate_author_name()
        category_name = generate_category_name()
        discount_price = generate_discount_price_count()
        price = generate_price_count()
        publish_date = generate_publish_date()
        
        author = Author.objects.get_or_create(
                    name=author_name
                )

        book = Book(
            title=title,
            author=Author.objects.get(name=author_name),
            publish_date=publish_date,
            price=price,
            discount_price=discount_price
        )

        book.save()

        category = Category.objects.get_or_create(name=category_name)

        book.categories.add(
            Category.objects.get(name=category_name))

    self.stdout.write(self.style.SUCCESS('Data imported successfully'))
        
     