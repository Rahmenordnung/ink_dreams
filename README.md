# ink_dreams

#### <a name="Description"></a>Description :

This project is built for Code Institute as a part of Full Stack Software Development Diploma course. Project was build using semantic HTML5, CSS3, JavaScript along with Python framework Django 2.2. For it I have been using Visual Studio Code that as a Source Code Editor for the local development. Heroku as a web plataform for the website deployment.

A small resumee of the features would be:

* Sign up, log-in as a user,don´t worry about your password you can reset it easely, view the books list, view the details of a book, add a book to shopping cart, Adjust the quantity of items in shopping cart, delete the item from the shopping cart, Pay for the desired products in shopping cart checkout, --------as a registered user see in the profile site, what products have been already bought.----
 

Search products (by 15 parts categories)
Vote to like / dislike products
Contact us via contact page


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
    
    --[Packages](#Packages)

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
  * [Local Deployment](#Local_Deployment)
* [The DOM](#The_DOM)
* [Challenges](#Challenges)
* [Bugs](#Bugs)
* [Acknowledgements](#Acknowledgements) 
 

#### <a name="Name"></a>Name :

Today in our days the books are not any more only wrote in paper but also digitally. Everything is changing, and it always has been like that. A tempestuous change through the ways of understanding a how the content of a message is transmited to us. Before we use to carve in stones, and now it feels like we don´t need anymore to write with our pens and hands, now we can just talk and that will be wrote. In anyway things will change, the old fashion way of doing things still will permeate our lives for a while. Until the books will disaprear they will contain ink, and this ink brings us dreams and make us dream further and that is why I chose as title for my work __Ink dreams__. 
 
 A link of the working project can be found [here](https://rahmenordnung.github.io/toy_storie_shop/)

---
## <a name="UX"></a>UX :

### <a name="User_Stories"></a>User Stories :

"Reading means dreaming by someone else's hand."  – Fernando Pessoa

"When you write, you show a world at your size" - Jesús Fernández Santos.

Reading means thinking with the alien brain instead of doing it with one's own. " Arthur Schopenhauer" 

.....

-The milestone proyect theme would be to have a look at the page and check as a user, an author, etc through a vast pallet of books, discovered them and let yourself onboard in new dreams and thoughts, by purchasing them.
-The custumer would be able also to contact and send us his thoughts and queries through a contact form.
-Any person can use the page and look around and serach easely with the help of pagination and search function through our book selection. If he doesn´t want to buy the product he can just chek the simple description and investigate perhaps about it. 

---
### <a name="Wireframes"></a>Wireframes :

You can find a pdf link for the wirefranes here: [Mockups](https://github.com/Rahmenordnung/toy_storie_shop/tree/master/assets/images/mockups)

---
##  <a name="Features"></a>Features

In the constuction of the project I have used the libraries donated by the Code institute, and other functional elements.


#### <a name="Current_Features"></a>Current Features ##


#### <a name="Existing_functionality"></a> Existing functionality ##

-- __Navbar__: Allows all users to easily navigate to the different sections of the website and interpretate the theme which relates them, regardless of which page they are currently on, simply by clicking the name of the area they wish to visit in the navbar(some of the areas will be limitted by a _@register required_ decorator). Also contain an logo that redirect to the home page.

-- __Full screen book list in card display__: Each book ispresented with image category author and price(and discount price if existing) in square formed cart. Each cart links to the detailed view of the book.

-- __Search bar/advanced search__: There is a _search bar_ in the home page that search by book title and an _advanced search_ page that leads the customer to a special page where one can specify more paramaeters by which one can search a book, ex production day, author, etc.

-- __Footer__: At the bootom of the page, this footer connect the user with the social media links, and presents the copyright. It also has a link to the contact form.

-- __Footer__: Informs the user that the site is hosted by Github Pages, and provides us a link to where they can view the source code on Github, and also a link to the dataset in a elegant dark green color.

-- __Contact Form__: A simple contact form with a query category selector name and subject. relized with django forms, that helps people getting in touch and improving the UX.

-- __Detail view of a book__ After clicking in any book on the book list page, you will be able to see the book cover in a big picture and on the other side the book description, the category tag, and the sticker tag which tries to resume in one word the story like a hashtag in socialmedia, the price/& discount price. There are two bottons add to cart and eliminate from cart that only can work if the user is registered and signed in. There also exists a section in the bottom site with additional information that can be useful.

-- __Registration and Sign in/out__: Is a security measure that ensure that all user will be registered, recorded and authorized to work with some functionallity of the page. In my case I used Django Allauth. 

-- __Reset password of a user__: Is realized with a Smtp code that sends a email to the customer that contains information and a link for the password reset, in case of a lost.

-- __Shopping_list__: Display a list of the products that have been added to the shopping trolley, that will be in the future purchased.
Here one can increse, diminish the product quantity, remove fully the book from the list, see the total, and by clicking in proceed to checkout will be redirected to provide information in order to purchase the products on the list. Or one can continue purchasing and so go back to the books list.

--__Checkout form (1)__: in the first page one will be able to introduce the personal adress details as well as the country where one comes from(done with django countries package). On the side it contains the total and a small resume of the pructs to be purchased. After clicking continue to purchase, it will lead you to the last site.

--__Checkout form (2)__: Here one will be able to process to payment with stripe, see the total of the products to be brought. After introducing the credit card number just click the submit payment.

--__Votes__--------------------------------------------------------------to do votes ???

--__Profile__------------------------------------------to do profile with sale list  ???

#### <a name="Coding_languages"></a>Current Features ##

-- [Django](https://www.djangoproject.com/) Django is an open source web framework written in Python that follows a model-view-presenter schema. 

-- [Python](https://www.python.org/)  Python is a general purpose programming language. Usefull for developing both desktop and web applications is designed with features to facilitate data analysis and visualization. Mostly Django is realized in python language, so the logic is mainly the same in the views pages, for instance

-- [HTML5](https://www.w3schools.com/html/html_intro.asp) --Hypertext Markup Language is the standard markup language for documents designed to be displayed in a web browser. I have useed it to create the templates, mostly

-- [CSS3](http://www.css3.info/) is a style sheet language used for describing the presentation of a document written in a markup language like HTML.Used to style the html templates

------------- [Javascript](https://www.javascript.com/) is a high-level, interpreted programming language that conforms to the ECMAScript specification. Used mostly with [Stripe](https://dashboard.stripe.com/) to deal withe payment- 
 
-- [MDBootstap](https://mdbootstrap.com/) is a framework created by Mozilla used to help you design websites faster and easier.

-- [jquery.js](https://jquery.com/) is a library of Java scripts that simplifies lots of its functions, the main differance with javascriptis that it performs many common scripting functions in fewer lines of codes. I have used the jquery present for the [MDB](https://mdbootstrap.com/) templates

-- [Font-awesome](https://fontawesome.com/) Font Awesome is a web font containing all the icons from the Twitter Bootstrap framework, and now many more. With it one can add usefull icons that improves the UX.

#### <a name="Packages"></a> Packages ##

This packages are included in the __requrements.txt__ files , thethat is needed in order to deploy the _django page_ to live platforms such as __Heroku__.

-- [Stripe] (https://dashboard.stripe.com/)Stripe is an online payment service, to enable secure payments using credit cards on the website. Stripe also uses a self-learning fraud prevention system.

-- [Django Allauth] (https://django-allauth.readthedocs.io/en/latest/installation.html/)                                         Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.

-- [Django country] (https://pypi.org/project/django-countries/) An object used to represent a country, instantiated with a two character country code, three character code, or numeric code. It can be compared to other objects as if it was a string containing the country code and when evaluated as text, returns the country code. Contains a URL to the flag.

-- [Django cryspy forms] (https://django-crispy-forms.readthedocs.io/en/latest/install.html)  Django-crispy-forms is a django application that lets you easily build, customize and reuse forms using your favorite CSS framework, without writing template code and without having to take care of annoying details.

-- [Django cryspy forms] (https://django-crispy-forms.readthedocs.io/en/latest/install.html)  Django-crispy-forms is a django application that lets you easily build, customize and reuse forms using your favorite CSS framework, without writing template code and without having to take care of annoying details.  

-- [Pillow] (https://pillow.readthedocs.io/en/3.0.x/installation.html/)  Pillow is a free library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats.

-------Travis
Travis CI is a hosted continuous integration service used to build and test software projects hosted at GitHub.
-------EmailJS
We use EmailJS to link up the modal contact form to an actual e-mail address---
------ pyrg???------ for heroku

----------------------------------------

## <a name="Features left to implement"></a>Features_left_to_implement ##

* First of all I like a lot the graphical distributions in general. So one of the thing that I would like to do is to implement more types of Charts, but for that I have to learn more abot javascript.

* I would like also to connect maybe more datasets and work with them

* Also is my intention to maybe work with geographical data in which I am interested.

* Also it would be nice also to make maybe graphics more complicated with more variables connected.

---
## <a name="Dataset"></a>Dataset

The data set has been exported from Kaggle. A link of the exact dataset used can be found here .>>[Kaggle](https://www.kaggle.com/kyanyoga/sample-sales-data)

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

__Go and play button__: When hovered changes color and adds margin around. When clicked hides the hole _start image_ and the _background page_ and displays the charts page that beginns with _intro.js tour_

__intro.js tour__ it will be displayed when firsly showing the charts page or each time we refresh it and it will guide the User, explain and show him the first steps that the User can do in order understand better the page and its purpose.

__Select bar__ When clicking have to display to indicated data from the dataset, and if clicked to filter throgh the selection and limit the other elements.

__Toggle button__ When clicked once it hides the respective card where the charts are contained, twice it shows it back again. This can be helpfull in order to ease the graphs display and their analysis.

__The charts__ are interactive and responsive and if clicked they will show the section clicked and if clicked back again that will go to the normal view again. And they will be responsive to mobile devices.

__Back to top button__ It will take the user when clicked to the top of the page. So that the user experience is improved in that one can move easily on top or down (with scrolling or navbarlinks) of the page.

__Reset button__ When clicked it resets the charts filtering selection.

__Footer__ It contains anchors, social media, dataset, main page that takes the User to the desired links.

## <a name="Deployment"></a> Deployment  #### 

This project is deployed on heroku: https://django-ecommerce-milestone.herokuapp.com/

#### <a name="Local_Deployment"></a>Local Deployment

In order to run this project __locally__ on your own system, you need following:

It's highly recommended to work in a virtual environment, but not absolutely required.

* Python 3.1.0 (the version that I used) to run the application
* PIP to install all requirements wit `pip install -r requirements.txt`
* GIT(hub) for cloning and version control and to download the repo in zip format

##### Next one should follow this steps in order to make this project work:
---

* Clone the repo with command git clone or donwloand the zip file
* Unpack the zip file and go to the file location and cd <path to folder>
* Create .env with the command in `python -m venv .env` in the terminal 
* Select the virtual environment in the interpreter
* Install all requirements with pip3 -r requirements.txt
* Launch the project python manage.py runserver
* The Django server has this url http://127.0.0.1:8000/
* Create .gitignore file where you will add all the files that you don´t want to be shared in github, such as Secret keys, virtual environments, or local databases, etc. In my case I created a env.py and that must be added in the SETTINGS from the main app (book_shop) and import env under import os 
* Make first steps saving(implementing) the data with: __python manage.py makemigrations__ and __python manage.py migrate__
* To use Django Admin Panel, you must generate a superuser:__python manage.py createsuperuser__



#### <a name="Developer_environment"></a> Developer environment  #### 

As for the external use of the program, the user should download first the Toys shop data base.csv file.
and upload then the above mentionated libraries, after that ,load the bootstap file and the dc.css as well as jquery so that the program should deploy as expected. 


------------HEroku----------------

---                                                                                                                                      

## <a name="Challenges"></a> Challenges  ## 

For me was something really exciting to work with data and create amazing graphics. Hard to find a good dataset, to learn at the beggining was the crossfilter, the reduce function, even to adjust the graphs to the cards had some issues for me as I am still a rookie. But the most challenging, and that is why I add it to the project was the map.js, whict took me long time , and still not is not brought to a sublime status, though a functional one. Displaying data in the data-grid was also a hard task for me.

## <a name="Bugs"></a> Bugs  ## 
I had some problems with the graphs display and the bootrap classes. 
Second problem was the size of the background image and it was because of the use of useless classes.
## <a name="Acknowledgements"></a> Acknowledgements  ## 
Carina_lead had a video about her project and that helped me when I was stucked in my page. At that time I had only the graphics done, but not a good display. And her call/video helped me.

Many thanks also to the Tutors, my mentor Guido Cecilio Bernal, and to the Code Institute Slack channel was invaluable!

