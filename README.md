# ink_dreams

[![Build Status](https://travis-ci.org/Rahmenordnung/ink_dreams.svg?branch=master)](https://travis-ci.org/Rahmenordnung/ink_dreams)


#### <a name="Description"></a>Description :

This project is built for Code Institute as a part of Full Stack Software Development Diploma course. Project was build using semantic HTML5, CSS3, JavaScript along with Python framework Django 2.2. For it I have been using _Visual Studio Code_ as a Source Code Editor for the _local development_. _Heroku_ as a web plataform for the _live website deployment_.

The code is meant to recreate an online book shop, such as Dubray or Easons. It is built upon mdboostrap (very similar to bootrap) templates, using all, or most of the techniques required for this last Milestone project. It takes the data saved and also saves the data in databases with the help of models and retrives it redirecting it via Urls, to the views and forms that at the same time display the data in html templates. That is the normal flow of a Django project.

#### Sumary :

* [Description](#Description)
* [Name](#Name)
* [UX](#UX)
* [User Stories](#User_Stories)
   - [Wireframes](#Wireframes)
* [Features](#Features)
  * [Current Features](#Current_Features)
 
    --[Existing_functionality](#Existing_functionality)
   
    --[Coding languages](#Coding_languages)
    
    --[Dependencies](#Dependencies)

    --[Libraries](#Libraries)
    
    --[Miscelaneous](#Miscelaneous)
    
    --[Google API](#Google_API)
    
* [Features left to implement](#Features_left_to_implement)    
* [Testing](#Testing)
  * [Responsiveness Testing](#Responsiveness_Testing)
  * [Code Testing](#Code_Testing)
  * [Ux Testing](#Ux_Testing)
* [Dataset](#Dataset)
* [Media](#Media)
* [Deployment](#Deployment)
  * [Deployment_local](#Deployment_local)
  * [Live Deployment](#Live_Deployment)
* [The DOM](#The_DOM)
* [Challenges](#Challenges)
* [Bugs](#Bugs)
* [Acknowledgements](#Acknowledgements) 
 

#### <a name="Name"></a>Name :

Today in our days the books are not any more only wrote in paper but also digitally. Everything is changing, and it never have been so many changes in our lives. A tempestuous change through the ways of understanding a how the content of a message is transmited to us. Before we use to carve in stones, and now it feels like we don´t need anymore to write with our pens and hands, now we can just talk and that will be wrote. In anyway things will change the old fashion way of doing things still will permeate our lives for a while. Until the books will disapear they will contain ink, and this ink brings us dreams and make us dream further and that is why I chose as title for my work __Ink dreams__. 
 
 A link of the working project can be found [here](https://rahmenordnung.github.io/toy_storie_shop/)

---
## <a name="UX"></a>UX :

### <a name="User_Stories"></a>User Stories :

"Reading means dreaming by someone else's hand."  – Fernando Pessoa

-- The user, book lover or not can open the page and look for a product, searching, filtering through them, finding what he wants, add it to a preliminatry chechout page, modify the amount, maybe delete the a item from the list, and purchase the product.
The user can easely go back from any page of the site back to the home page

"When you write, you show a world at your size" - Jesús Fernández Santos.

-- The custumer would be able also to contact and send us his thoughts and queries through a contact form.

Reading means thinking with the alien brain instead of doing it with one's own. " Arthur Schopenhauer"

--Any person can use the page and look around and serach easely with the help of pagination and search function through our book selection. If he doesn´t want to buy the product he can just check the simple description and investigate perhaps about it. He also can with perhaps more information through the social media links present in the footer.

### <a name="Wireframes"></a>Wireframes :

You can find the link for the project wirefranes here: [Mockups](https://github.com/Rahmenordnung/ink_dreams/tree/master/static/images/mockups/project_mockup)

For the django project I have made also two sketches: 
--One is of the structural relations tree of my __models.py__ file, in order to clarify the conextions between elements in the database.
[Models relations tree](https://github.com/Rahmenordnung/ink_dreams/tree/master/static/images/mockups/django_flow_sketch)

--The second is about the normal workflow of a Django project, that, of course I had to learn in order to apply in the best way I could.
[Django normal workflow](https://github.com/Rahmenordnung/ink_dreams/blob/master/static/images/mockups/django_flow_sketch/django_flow.jpg)

---
##  <a name="Features"></a>Features

In the constuction of the project I have used the libraries donated by the Code institute, and other functional elements.

A small resumee of the features would be:

* Sign up, log-in as a user,don´t worry about your password you can reset it easely, view the books list, view the details of a book, add a book to shopping cart, Adjust the quantity of items in shopping cart, delete the item from the shopping cart, Pay for the desired products in shopping cart checkout, as a registered user see in the profile site, what products have been already bought.
 

-----Search products (by 15 parts categories)------------------
-----------Vote to like / dislike products-----------

### <a name="Current_Features"></a>Current Features ###

#### <a name="Existing_functionality"></a> Existing functionality ##

-- __Navbar__: Allows all users to easily navigate to the different sections of the website and guide themselvs by the name which relates them, regardless of which page they are currently on, simply by clicking the name of the area they wish to visit in the navbar(some of the areas will be limitted by a _@register required_ decorator). Also contain an logo that redirects to the home page.

-- __Full screen book list in card display__: Each book is presented with hoverable image category author and price(and discount price if existing) in square formed cart. Each cart links to the detailed view of the book.

-- __Search bar/advanced search__: There is a _search bar_ in the home page that search by book title and an _advanced search_ page that leads the customer to a special page where one can specify more parameters by which one can search a book, ex production day, author, price etc.

-- __Footer__: Informs the user that the site is hosted by Github Pages, and provides us a link to where they can view the source code on Github, and also a link to the dataset in a elegant dark green color.

-- __Contact Form__: A simple contact form with a query category selector name and subject. realized with django forms, that helps people getting in touch with the site, improving  in this way the UX.

-- __Detail view of a book__ After clicking in any book on the book list page, you will be able to see the book cover in a big picture and on the other side the book description, the category tag, and the sticker tag which tries to resume in one word the story like a hashtag in socialmedia, the price/& discount price. There are two bottons add to cart and eliminate from cart that only can work if the user is registered and signed in. There also exists a section in the bottom site with additional information that can be useful.

-- __Registration and Sign in/out__: Is a security measure that ensure that all user will be registered, recorded and authorized to work with some functionallity of the page. In my case I used Django Allauth. 

-- __Reset password of a user__: Is realized with a Smtp code that sends a email to the customer that contains information and a link for the password reset, in case of a lost.

-- __Shopping_list__: Display a list of the products that have been added to the shopping trolley, that will be in the future purchased.
Here one can increse, diminish the product quantity, remove fully the book from the list, see the total, and by clicking in proceed to checkout will be redirected to provide information in order to purchase the products on the list. Or one can continue purchasing and so go back to the books list.

--__Checkout form (1)__: in the first page one will be able to introduce the personal adress details as well as the country where one comes from(done with django countries package). On the side it contains the total and a small resume of the products to be purchased. After clicking continue to checkout, it will lead you to the last site.

--__Checkout form (2)__: Here one will be able to process to __payment with stripe__, see the total of the products to be brought. After introducing the credit card number just click the submit payment and the desired product will be ordered and the purchase registered in the Stripe records.

--__Messages__: After each action that involves a interaction with the database and the server there are messages implemented that improve the UX, and make easier the understanding of the processes carried out in the background.

--__Profile__ The user profile page is a simple list specific for each user that has a an account in our site. Is meant to display a resumee with detail of each transaction carried out by the user.

------------------------__Category filter selector__ it displays all the categories/genres by which the books are separated. Each book has a genre assigned, and therefor a user can identify better a group of books related by the genre. The category display works filtered by genre by clicking on each of them.

--__Votes__--------------------------------------------------------------to do votes ???


#### <a name="Coding_languages"></a>Current Features ##

-- [Django](https://www.djangoproject.com/) Django is an open source web framework written in Python that follows a model-view-presenter schema. 

-- [Python](https://www.python.org/)  Python is a general purpose programming language. Usefull for developing both desktop and web applications is designed with features to facilitate data analysis and visualization. Mostly Django is realized in python language, so the logic is mainly the same in the views pages, for instance

-- [HTML5](https://www.w3schools.com/html/html_intro.asp) --Hypertext Markup Language is the standard markup language for documents designed to be displayed in a web browser. I have useed it to create the templates, mostly

-- [CSS3](http://www.css3.info/) is a style sheet language used for describing the presentation of a document written in a markup language like HTML.Used to style the html templates

-- [Javascript](https://www.javascript.com/) is a high-level, interpreted programming language that conforms to the ECMAScript specification. Used mostly with [Stripe](https://dashboard.stripe.com/) to deal withe payment- 
 
-- [jquery.js](https://jquery.com/) is a library of Java scripts that simplifies lots of its functions, the main differance with javascriptis that it performs many common scripting functions in fewer lines of codes. I have used the jquery present for the [MDB](https://mdbootstrap.com/) templates

-- [Font-awesome](https://fontawesome.com/) Font Awesome is a web font containing all the icons from the Twitter Bootstrap framework, and now many more. With it one can add usefull icons that improves the UX.

-- [MDBootstap](https://mdbootstrap.com/) is not a coding language but provides such a big help to the code beeing a framework created by Mozilla used to help you design websites faster and easier.

#### <a name="Dependencies"></a> Dependencies ##

This packages are included in the __requrements.txt__ files , that is needed in order to deploy the _django page_ to live platforms such as __Heroku__.

-- [Stripe](https://dashboard.stripe.com/) is an online payment service, to enable secure payments using credit cards on the website. Stripe also uses a self-learning fraud prevention system.

-- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html/)
Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.

-- [Django country](https://pypi.org/project/django-countries/) An object used to represent a country, instantiated with a two character country code, three character code, or numeric code. It can be compared to other objects as if it was a string containing the country code and when evaluated as text, returns the country code. Contains a URL to the flag.

-- [Django cryspy forms](https://django-crispy-forms.readthedocs.io/en/latest/install.html)  Django-crispy-forms is a django application that lets you easily build, customize and reuse forms using your favorite CSS framework, without writing template code and without having to take care of annoying details.

-- [Pillow](https://pillow.readthedocs.io/en/3.0.x/installation.html/) Pillow is a free library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats.

-- [Psycopg](https://pypi.org/project/psycopg2/) Package to connect to Postgress databases. Is the most popular PostgreSQL database adapter for the Python programming language. Its main features are the complete implementation of the Python DB API 2.0 specification and the thread safety (several threads can share the same connection).

--[urllib3](https://urllib3.readthedocs.io/en/latest/) brings many critical features that are missing from the Python standard libraries, such as File uploads with multipart encoding, Proxy support for HTTP and SOCKS, 100% test coverage, and many others

## <a name="Dataset"></a>Dataset

Django is a flexible framework for quickly creating Python applications. _By default_,locally Django applications are configured to store data into a lightweight [SQLite](https://www.sqlite.org/index.html) database file.

When we _deploy to Heroku_ one must chose a new data base because that it will be used in the live environment, and not the old one SQLite that is used by default and locally. The easiest way and the cheapes is to use [Postgresql](https://www.postgresql.org/)


-------Travis
Travis CI is a hosted continuous integration service used to build and test software projects hosted at GitHub.
-------EmailJS
We use EmailJS to link up the modal contact form to an actual e-mail address---
------ pyrg???------ for heroku

----------------------------------------

## <a name="Features left to implement"></a>Features_left_to_implement ##

* I think this last milestone represents the reallity of the web pages in our days, because it accomplish, even in basic way the most functionality of a real page on the web. I would like to make the page as complete as possible making all the functionallity work like it would work for real customers.

* I would like to implement a the _django.translator package_ in order be able to present the page in multiple languages, without needing to recur to google translate. I think the translator package would be improving the page for users who don´t speek english or look for books in other langage that english.

* In the future adding some votes to the page would make the interaction with the customer stronger. Also a comments page won´t be bad.This comments would be giving a better idea of the customers feedbacks.

* I would also like to present a ranking with the best books in the main page. and filter through them.

---

## <a name="Media"></a> Media  ##
All the images used in the project are taken from Google images page and there are free of copyright.

In this project I used just one image __[link](https://papers.co/ipad/mm13-old-car-street-vintage/)__  

## <a name="Testing"></a> Testing  ## 

#### <a name="Responsiveness_Testing"></a> Responsiveness Testing  ## 

The responsiveness of the website was tested on Chrome developer tool and also in the Mozzila developer tool.

At this stage, the positioning of the footer and background image  and charts cards was tested on the following devices:

Blackberry Playbook
Galaxy sIII, NOte II, 3
Laptop with HiDPI
Microsoft Lumia 550
Nexus 4,5,6,10, etc
Nokia Lumia, N9
iPhone 5/SE,6 7,8,X
iPad, /Pro/ Mini
etc

The full page is responsive in small, medium, and big devices. The charts are fully responsive thanks to the __.useViewBoxResizing(true)__ property added in all the charts. Also I create this responsivness with help of the bootrap cards and classes used in their grid system. The selector bar, navbar and footer I edited myself and created some media queries with css help as I learned in previous modules.

#### <a name="Code_Testing"></a> Code Testing  ####
The HTML was validated using the HTML Validator.

The CSS was validated using the CSS Validator. In total, 1 issues was found. This has to do with the parsing of a property. But as it doesn´t really affect the project I considerated to ignore it.

TheJavaScript files were tested using JSHint.com. Initially, 1 warnings were detected: Duplicate key 'mapTypeId'. But that is the normal type of expression for map.js. The rest is clean.

#### <a name="Ux_Testing"></a> Ux Testing ####

The normal functionality of the page has been tested through this tests:

__Full Background start image__: When hovered over it shows a dinamic effect contains a button.


__Select bar__ When clicking have to display to indicated data from the dataset, and if clicked to filter throgh the selection and limit the other elements.

__Reset button__ When clicked it resets the search filtering selection.

__Footer__ It contains anchors, social media, dataset, main page that takes the User to the desired links.

------------
__Stripe__ payment function has been verified with a test card and all transactions show up on the Stripe dashboard.

[Stripe test](https://github.com/Rahmenordnung/ink_dreams/tree/master/static/images/test_images)

## <a name="Deployment"></a>Deployment #### 

This project is deployed on heroku: https://django-ecommerce-milestone.herokuapp.com/

---

### <a name="Deployment_local"></a>Local Deployment

In order to run this project __locally__ on your own system, you need following:

It's highly recommended to work in a virtual environment, but not absolutely required.

* Python 3.7.4 (the version that I used) to run the application
* PIP to install all requirements wit `pip install -r requirements.txt`
* GIT(hub) for cloning and version control and to download the repo in zip format

##### Next one should follow this steps in order to make this __project work(locally)__:

* Clone the repo with command git clone or donwloand the zip file
* Unpack the zip file and go to the file location and cd <path to folder>
* Create .env with the command in `python -m venv .env` in the terminal 
* Select the virtual environment in the interpreter
* Install all requirements with `pip3 -r requirements.txt`
* Launch the project python manage.py runserver
* The Django server has this url http://127.0.0.1:8000/
* Create .gitignore file where you will add all the files that you don´t want to be shared in github, such as Secret keys, virtual environments, or local databases, etc. In my case I created a env.py and that must be added in the SETTINGS from the main app (book_shop) and import env under import os 
* Make first steps saving(implementing) the data with: `__python manage.py makemigrations__` and `__python manage.py migrate__`
* To use Django Admin Panel, you must generate a superuser:__python manage.py createsuperuser__

---

### <a name="Live_Deployment"></a>Live Deployment  ###

Heroku is a cloud application platform, it is basically a Platform-as-a-Service (PaaS). They support several programming languages, including Python. It is very easy to deploy Django applications on Heroku. They also offer a free plan, which is quite limited, but it is great to get started and to host demos of Django applications. 

##### The following section describes the process to deploy this __project to Heroku__. #####

Add a Procfile in the project root or create a file named Procfile in the project root with the following content:
```
web: gunicorn ink_dream.wsgi
```
Add __requirements.txt__ file with all the __Dependencies__ in the project root:
Ensure all required technologies are installed locally, as per the __requirements.txt__ file.
If you are using a __virtualenv and pip__ you can simply run:
```
pip freeze > requirements.txt
```
##### Heroku usefull packages (used solely for Heroku)

* Add __Gunicorn__ to requirements.txt;
Green Unicorn, commonly shortened to "Gunicorn", is a Web Server Gateway Interface (WSGI) server implementation that is commonly used to run Python web applications.

* Configure __whitenoise__ to serve static files. ---------------------With a couple of lines of config WhiteNoise allows your web app to serve its own static files, making it a self-contained unit that can be deployed anywhere without relying on nginx, Amazon S3 or any other external service. (Especially useful on Heroku, OpenShift and other PaaS providers.)-----where????

* __dj-database-url__: This simple Django utility allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application. So it connects to the database Url.

Now follow this steps:
* Using the CLI, login to Heroku, using __'heroku login'__ command. You'll be prompted to enter any key to go to your web browser to complete login. Input Heroku login details.
* Create new Heroku app, using __'heroku apps:create appname'__ command.
* In Heroku, select resources. Type Postgres and select __Heroku Postgres__ > Hobby - Free. You will use this data base as the live database instead of the default __dqlite3__ provided by any coding program when starting the project in django.
Creating a new DB will lose all database information stored within the IDE. You will be reqired to re-update this information when the project is hosted via Heroku.
*Select Settings, Reveal Config Vars. Copy Postgres DB url and paste into env.py.
Also add all the keys, public or secret or any values present(for Smtp, ex) in the locally hosted env.py in the heroku settings, that will worl as the new livw environment
* Execute __python manage.py makemigrations__ and __python3 manage.py migrate__, to create a new DB.
* Execute __python3 manage.py createsuperuser__ and populate as required, to create a new superuser.
* Update allowed hosts within settings.py with your Heroku host name. Example, ALLOWED_HOSTS = [http://127.0.0.1:8000/, 'mythware.herokuapp.com'].------------------
* Push project to Heroku, using __push -u heroku master__ command.
In Heroku, select settings, select Domain URL, NOT Git URL to view your hosted application.

* Deployed via Heroku: ink-dream.

---                                                                                                                                      
## <a name="Challenges"></a> Challenges  ## 

I founded them __"Django and its included batteries"__, Meaning that is better organized and therefor is easier the extend the code to different functionallity, is easier to go big, without big effort.__"I almost lose those bateries"__, For a rookie like me, it sometimes hard to control differnt apps one with another. That is the main reason I decided to keep all the book related views in one app instead of dividing them in 2 or 3 apps. For me was a chalLenge to see clearely the relation between each of them and that is why I consideratd is better to keep them in the same code page

## <a name="Bugs"></a> Bugs  ## 
I had some problems with search and category filter. 
Second problem was that the Heroku deployment wasn´t successful several times but at the end I managed to solve it.
## <a name="Acknowledgements"></a> Acknowledgements  ## 
The project was inspired from a page that I am always using, and even though I haven´t recreated all the functionality the structure I tried to make it similar as the one from * [Open library](https://openlibrary.org/)

For this project I have used the video offered by Code Institute, as well as other sources such as: 

* [Django documentation](https://docs.djangoproject.com/en/2.2/)
* [Oreily](https://www.oreilly.com/library/view/beginning-django-e-commerce/9781430225355/ch08.html)
* [Stackoverflow](https://stackoverflow.com/questions/38006125/how-to-implement-search-function-in-django), also used for pagination and many , many other functionality
* [simpleisbetterthancomplex](https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html)(https://www.youtube.com/watch?v=JBhpo0o1Ajg&t=416s)
* [Just Django](https://www.youtube.com/watch?v=vccUP3jdpBg)
* [Freak Network](https://www.youtube.com/watch?v=MPyHEMD7V6Q&list=PLj-jdGgxSLAkO-5EweQDdkyoF9wpI6vbj)
* [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04)
* [Max Goodridge](https://www.youtube.com/watch?v=nwpLCa79DUw)

Many thanks also to __the Tutors, my _mentor Guido Cecilio Bernal_, and to the Code Institute Slack channel was invaluable__!

