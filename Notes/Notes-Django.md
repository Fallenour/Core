# Notes-Django

## 📖 Tour Guide

| Directory Type | Directory |
| ----------- | ----------- |
| Resources| [Resource Directory](#resource-directory) |
| Projects | [Project Directory](#project-directory) |

---
---

# [↑](#tour-guide)Project Directory
> A curated list of my django notes, practice projects, and sample code that I actively contribute to or plan to. Maintained by <a rel="" href="https://github.com/fallenour">Logan Hicks</a>.

## 📖 Table of Contents

| Component                   | Description                                                       | Link                              |
|-----------------------------|-------------------------------------------------------------------|-----------------------------------|
| Model View Controller (MVC) | How Django Loads, manages, and handles requests                   | [Link](#-model-view-controller)   |
| Models                      | How Django structures data                                        | [Link](#-models)                  |
| Views                       | How Django structures requests & renders                          | [Link](#-views)                   |
| Controllers                 |                                                                   | [Link](#-controllers)             |
| URLs                        | How Django manages endpoints                                      | [Link](#-urls)                    |  
| Database                    | How Django manages data                                           | [Link](#-databases)               |
| Settings                    | How Django is configured                                          | [Link](#-settings)                |
| Middleware                  | How Django manages middleware                                     | [Link](#-middleware)              |
| Secure Coding               | Django Secure Coding Best Practices                               | [Link](#-secure-coding)           |  
| Django Unit Tests           | Guides on how to build unit, function, and view testing of Django | [Link](#-django-unit-tests)       |
| Dockerizing Django          | Best Practices on Dockerizing Django                              | [Link](#-dockerizing-django)      |
| Deploying to Production     | Best Practices for Deploying to Production                        | [Link](#-deploying-to-production) |

---
---

## [↑](#-table-of-contents) Model View Controller
> Model View Controller Notes for Django

---
### Overview 
- <additional notes here>
---

| Component   | Description | Link |
| ----------- | ----------- | ----------- |
| Model View Controller (MVC) Basics | Understanding Model View Controller (MVC) Basics | [Link](https://<webaddress>) |


---
---

## [↑](#-table-of-contents) Models
> Models Notes for Django

---
### Overview 
- <additional notes here>
---

| Component   | Description | Link |
| ----------- | ----------- | ----------- |
| Models Basics | Understanding Models Basics | [Link](https://<webaddress>) |
| Primary Keys | Understanding Primary Keys | [Link](https://<webaddress>) |
| Foreign Keys | Understanding Foreign Keys | [Link](https://<webaddress>) |

  - [Link](https://docs.djangoproject.com/en/4.1/topics/db/models/) Models
  - [Link](https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_many/) Many to Many Examples
  - [Link](https://learndjango.com/tutorials/django-best-practices-referencing-user-model) Best Practices Referencing User Models
  - [Link](https://stackoverflow.com/questions/6928692/how-to-express-a-one-to-many-relationship-in-django) Referncing One to Many Model
  - [Link](https://docs.djangoproject.com/en/3.2/ref/models/fields/#foreignkey) Foreign Keys

---
---
  

## [↑](#-table-of-contents) Views
> Views Notes for Django

---
### Overview 
- <additional notes here>
---

| Component                             | Description | Link |
|---------------------------------------| ----------- | ----------- |
| Views Basics                          | Understanding Views Basics | [Link](https://<webaddress>) |
| Class Based Views (CBVs)              | Understanding Class Based Views | [Link](https://<webaddress>) |
| Function Based Views (FBVs)           | Understanding Function Based Views | [Link](https://<webaddress>) |
| CBVs vs FBVs                          | Understanding the differences of CBVs & FBVs | [Link](https://<webaddress>) |
| Mixins Basics                         | Understanding Mixins Basics | [Link](https://<webaddress>) |
| Class Based Views - Permission Checks | Understanding Mixins Basics | [Link](https://<webaddress>) |

# View Basics
> Text place holder
# Class Based Views
> text place holder

Types of Class Based Views
--------------------------


| Component     | Base Use Case                                       | Link                   |
|---------------|-----------------------------------------------------|------------------------|
| TemplateViews | Static Pages or GET Requests                        | [Link](#-TemplateView) |
| RedirectViews | Redirects to a given URL                            | [Link](#-RedirectView) |
| DetailViews   | Present detail of a single model instance           | [Link](#-DetailView)   |
| ListViews     | Present a list of objects                           | [Link](#-ListView)     |
| FormViews     | Displaying a Form. Best used for message/emails/EDA | [Link](#-FormView)     |
| CreateViews   | Displaying a Form. Best used to create objects      | [Link](#-CreateView)   |
| UpdateViews   | Best used for adding/updating database tables       | [Link](#-UpdateViews)  |


<br/>

### TemplateView
***

TemplateView()
- When you might use Template.View()?
- Generic View to show static pages
- Pages that use GET requests
- Not generally used:
  - Show a form on a page
  - Create/updates information (better options)

Using directly within URL Configuration
- TemplateView()
- Pass changes to class-based view as_view()
- Arguments passed to as_view() will override attributes set on the class.
  - Example: 
  We set template_name on the TemplateView
  
##### Urls.py


    from django.urls import path
    from django.views.generic import TemplateView

    app_name = 'cbv'

    urlpatterns = [
        # extra_content Attribute from ContentMixin - key
        path('ex1', TemplateView.as_view(template_name="ex1.html", extra_context={'title':'Custom Title'})),
        path('ex2', Ex2View.as_view(), name='ex2'),
    ]

#### Views.py


    from django.views.generic.base import TemplateView
    from cbv.models import Post

    class Ex2View(TemplateView)
        
        template_name = "ex2.html"
        
        # template_engine = The NAME of a template engine to use for loading the template.
        # response_class = Custom Template loading or custom context object instatiation
        # content_type = Default Django uses 'text/html'

        """ get_context_data(**kwargs) is a method inherited from ContentMixin """

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['posts'] = Post.objects.get(id=1)
            context['data'] = "Context Data for Ex2"
            return context

---

### RedirectView
***

RedirectView()
- Redirects to a given URL.
- Inherited methods and attributes:
  - django.views.generic.base.View

Why get_redirect_url?
- django.views.generic.base.View
- Method Flowchart
  - setup() (Performs ky view initialization)
  - dispatch() (accepts a request/response)
  - http_method_not_allowed()(HTTP Support method)
  - get_redirect_url()(Construct target URL for redirection)

Method Resolution Order - basically the order python looks for a method in the hierarchy of classes.

get_redirect_url
- get_redirect_url() # first checks to see if URL attribute is set.
  - URL is not set?
    - get_redirect_url() reverse the pattern_name

##### Urls.py


    from django.urls import path
    from django.views.generic import TemplateView, RedirectView
    from cbv.views import Ex2View, PostPreLoadTaskView, SinglePostView

    app_name = 'cbv'

    urlpatterns = [
        # extra_content Attribute from ContentMixin - key
        path('ex1', TemplateView.as_view(template_name="ex1.html", extra_context={'title':'Custom Title'})),
        path('ex2', Ex2View.as_view(), name='ex2'),
        path('rdt', RedirectView.as_view(url='http://youtube.com/veryacademy'), name='go-to-very'),
        path('ex3/<int:pk>/', PostPreLoadTaskView.as_view(), name='redirect-task'),
        path('ex4/<int:pk>/', SinglePostView.as_view(), name='singlepost'), # single post page
    ]


#### Views.py


    from django.views.generic.base import TemplateView, RedirectView
    from cbv.models import Post
    from django.shortcuts import get_object_or_404
    from django.db.models import F

    class Ex2View(TemplateView)
        
        template_name = "ex2.html"
        
        # template_engine = The NAME of a template engine to use for loading the template.
        # response_class = Custom Template loading or custom context object instatiation
        # content_type = Default Django uses 'text/html'

        """ get_context_data(**kwargs) is a method inherited from ContentMixin """

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['posts'] = Post.objects.get(id=1)
            context['data'] = "Context Data for Ex2"
            return context

    class PostPreLoadTaskView(RedirectView):
    
        # Everything in this section thats definable (by the = sign) is known as an attribute
        # url = 'http://youtube.com/veryacademy' ## Url can be sourced here, or as attribute in URl.py
        pattern_name = 'cbv:singlepost'
        # permanent = HTTP status code returned (True = 301, False = 302, Default = False)
        
        def get_redirect_url(self, *args, **kwargs):
            # post = get_object_or_404(Post, pk=kwargs['pk'])
            # post.count = F('count') + 1
            # post.save()

            post = Post.objects.filter(pk=kwargs['pk'])
            post.update(count=F('count') + 1)

            return super().get_redirect_url(*args, **kwargs)


    class SinglePostView(TemplateView):

        template_name = "ex4.html" # single.html

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['posts'] = get_object_or_404(Post, pk=self.kwargs.get('pk'))
            return context



### DetailView
***

DetailView()
Application
- Present Detail of a single model instance
- intended to be used with one object only (one item from a list of items)
- Must be called - by object primary key (pk)) or its  slug in the URLConf
  - path('list/<int:pk>/',views.XYZDetailView.as_view(), name= "xyz")
- Not Tpyically used for:
  - Page has a form
  - Used to return, update or create data
  - DetailView shoudl not be paginated

Most ideal applicatino is when you call event in events, and have all the events listed,
and you click on one. That page that loads is best as a DetailView. Blog post, Book item from a list, etc.

DetailView MRO
- Method MRO
- setup()
- dispath()
- http_method_not_allowed()
- get_templates_names()
- get_slug_field()
- get_queryset()
- get_object()
- get_context_object_name()
- get_context_data()
- get()
- render_to_response()

##### Models.py

    from django.db import models
    
    class Books(models.Model):
        # Example Model Only
        title = models.CharField(max_length=100)
        slug = models.SlugField(null=True)
        genre = models.CharField(max_length=100)
        author = models.CharField(max_length=100)
        isbn = models.CharField(max_length=100)
        count = models.IntegerField(null=True, default=0)



##### Urls.py
    from django.urls import path
    from .views import IndexView, BookDetailView
    
    app_name = 'books'
    
    urlpatterns = [
        path('', IndexView.as_view(), name='index'),
        path('<slug:slug>/', BookDetailView.as_view(), name='book-detail'),
    ]
##### Views.py

    from django.shortcuts import render
    from django.views.generic.base import TemplateView
    from books.models import Books
    
    class IndexView(TemplateView):
        
        template_name = "home.html"
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['books'] = Books.objects.all()
            return context

    class BookDetailView(DetailView):
        
        model = Books
        template_name = "book-detail.html" ## Note that if you dont stipulate what template to use, Django will by default attempt to define one for one, as in it will decide what it thinks the name should be for the template, and attempt to find it.
        context_object_name = 'book'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            
            post = Books.objects.filter(slug=self.kwargs.get('slug'))
            post.update(count=F('count') + 1)

            context['time] = timezone.now()

            return context
### ListView
***
ListView()
Application
- Present/Display a list of objects
- Intended to be used to output multiple objects
- ListView can be paginated

Not Typically used for:
- Page has a form
- Used to return, update or create data

ListView MRO
Method Flowchart
- setup()
- dispath()
- http_method_not_allowed()
- get_template_names()
- get_queryset()
- get_context_object_name()
- get_context_data()
- get()
- render_to_response()

##### Models.py

    from django.db import models
    
    class Books(models.Model):
        # Example Model Only
        title = models.CharField(max_length=100)
        slug = models.SlugField(null=True)
        genre = models.CharField(max_length=100)
        author = models.CharField(max_length=100)
        isbn = models.CharField(max_length=100)
        count = models.IntegerField(null=True, default=0)



##### Urls.py
    from django.urls import path
    from .views import IndexView, BookDetailView, GenreView
    
    app_name = 'books'
    
    urlpatterns = [
        path('', IndexView.as_view(), name='ex2'),
        path('g/<str:genre>', GenreView.as_view(), name='genre'),
        path('<slug:slug>/', BookDetailView.as_view(), name='book-detail'),
    ]
##### Views.py

    from django.views.generic.base import TemplateView 
    from django.views.generic.base import DetailView
    from django.views.generic.base import ListView
    from books.models import Books
    from django.db.models import F
    from django.utils import timezone
    
    class IndexView(ListView):
        
        model = Books
        template_name = "home.html" # if you use {% for book in object_list %} that wil laod all the books in the template
        context_object_name = 'books' # if you use {% for book in books %} that will load all the books the same as above in the template.
        paginate_by = 4 # this setting allows you to configure how many objects will load per page.
        # queryset = Books.objects.all()[:2] # this tells django that you only want to see 2. Evn though there are 4 of them, it iwll only show you 2.

        def get_queryset(self): # These two lines does the exact same thing that the queryset above does.
            return Books.objects.all()[:2]

    class BookDetailView(DetailView):
        
        model = Books
        template_name = "book-detail.html" ## Note that if you dont stipulate what template to use, Django will by default attempt to define one for one, as in it will decide what it thinks the name should be for the template, and attempt to find it.
        context_object_name = 'book'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            
            post = Books.objects.filter(slug=self.kwargs.get('slug'))
            post.update(count=F('count') + 1)

            context['time] = timezone.now()

            return context

    class GenreView(ListView):

        model = Books
        template_name = 'home.html'
        context_object_name = 'book'
        paginate_by = 2 # Pagination Over-ride

        def get_queryset(self, *args, **kwargs): # These two lines does the exact same thing that the queryset above does.
            return Books.objects.filter(genre__icontains=self.kwargs.get('genre'))


### FormView
***
FormView()
Application
- Display a form
  - On error -> redisplays the form with validation errors;
  - On success -> redirects to a new URL

Not typically used for:
- Not displaying a form page
- Saving data to a database

##### Models.py

    from django.db import models
    from django.template.defaultfilters import slugify
    
    class Books(models.Model):
        # Example Model Only
        title = models.CharField(max_length=100)
        slug = models.SlugField(null=True)
        genre = models.CharField(max_length=100)
        author = models.CharField(max_length=100)
        isbn = models.CharField(max_length=100)
        count = models.IntegerField(null=True, default=0)

        def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = slugify(self.title)
            return super().save(*args, **kwargs)



##### Urls.py
    from django.urls import path
    from .views import IndexView, BookDetailView, GenreView, AddBookView
    
    app_name = 'books'
    
    urlpatterns = [
        path('', IndexView.as_view(), name='ex2'),
        path('add/', AddBookView.as_view(), name='add'),
        path('g/<str:genre>', GenreView.as_view(), name='genre'),
        path('<slug:slug>/', BookDetailView.as_view(), name='book-detail'),
    ]
##### Views.py

    from django.views.generic.base import TemplateView 
    from django.views.generic.detail import DetailView
    from django.views.generic.list import ListView
    from django.views.generic.edit import FormView
    from books.models import Books
    from .forms import AddForm
    from django.db.models import F
    from django.utils import timezone
    
    
    class AddBookView(FormView):

        template_name = 'add.html'
        form_class = AddForm
        success_url = '/books/'

        def form_valid(self, form):
            form.save()
            return super().form_valid(form)

    class IndexView(ListView):
        
        model = Books
        template_name = "home.html" # if you use {% for book in object_list %} that wil laod all the books in the template
        context_object_name = 'books' # if you use {% for book in books %} that will load all the books the same as above in the template.
        paginate_by = 4 # this setting allows you to configure how many objects will load per page.
        # queryset = Books.objects.all()[:2] # this tells django that you only want to see 2. Evn though there are 4 of them, it iwll only show you 2.

        def get_queryset(self): # These two lines does the exact same thing that the queryset above does.
            return Books.objects.all()[:2]

    class BookDetailView(DetailView):
        
        model = Books
        template_name = "book-detail.html" ## Note that if you dont stipulate what template to use, Django will by default attempt to define one for one, as in it will decide what it thinks the name should be for the template, and attempt to find it.
        context_object_name = 'book'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            
            post = Books.objects.filter(slug=self.kwargs.get('slug'))
            post.update(count=F('count') + 1)

            context['time] = timezone.now()

            return context

    class GenreView(ListView):

        model = Books
        template_name = 'home.html'
        context_object_name = 'book'
        paginate_by = 2 # Pagination Over-ride

        def get_queryset(self, *args, **kwargs): # These two lines does the exact same thing that the queryset above does.
            return Books.objects.filter(genre__icontains=self.kwargs.get('genre'))

##### Forms.py
    from django import forms
    from .models import Books
    
    class Addform(forms.ModelForm):
    
        class Meta:
            model = Books
            fields = ('title', 'genre', 'author', 'isbn')
    
            widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'genre': forms.TextInput(attrs={'class': 'form-control'}),
                'author': forms.TextInput(attrs={'class': 'form-control'}),
                'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            }
##### add.html

    {% extends "base.html" %}
    {% block content %}
    <div class="container" style="max-width:600px">
      <div class="px-2 py-3 pt-md-5 pb-md-4 mx-auto text-center">
        <h1 class="display-4">All Books</h1>
        <p class="lead"> A range of wonderful programming books to help you learn Javascript.</p>
      </div>
      <div class="py-5">
        <div class="row">
          <div class="col-12">
            <form method="post">
              {% csrf_token %}
              {{ form.as_p }} ### This will wrap everything in a p tag
              <input type="submit">
            </form>
          </div>
        </div>
      </div>
    </div>
    {% endblock %}


### CreateView
***
CreateView()
Applications:
- A view - displays a form for creating an object
- Purpose of this view is to create objects

Not Typically used for:
- Not displaying a form page

CreateView vs FormView
FormView
- Leads toa  process -> Email being sent
CreateView
- Lead to an objet being saved to the db
- Displays a Form
  - For Creating an object
  - Redisplaying validation errors (if any)
  - Saving the object
- Avoid Boilerplate Code
- Succinct and more maintainable code

CreateView vs FormView
- Inherited Methods and Attributes

CreateView
- edit.BaseCreateView
- detail.SingleObjectTemplateResponseMixin
- edit.ModelFormMixin
- detail.SingleObjectMixin
- base.TemplateResponseMixin
- edit.FormMixin
- edit.ProcessFormView
- base.View

FormView
- edit.BaseFormView
- base.TemplateResponseMixin
- edit.FormMixin
- edit.ProcessFormView
- base.View

Differentiating the CreateView
- Provides a mechanism for looking up an object associated with the current HTTP Request.
- Has access to the:
  - Model
  - queryset attributes
- Provides manipulation of the model data


##### Models.py

    from django.db import models
    from django.template.defaultfilters import slugify
    
    class Books(models.Model):
        # Example Model Only
        title = models.CharField(max_length=100)
        slug = models.SlugField(null=True)
        genre = models.CharField(max_length=100)
        author = models.CharField(max_length=100)
        isbn = models.CharField(max_length=100)
        count = models.IntegerField(null=True, default=0)

        def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = slugify(self.title)
            return super().save(*args, **kwargs)



##### Urls.py
    from django.urls import path
    from .views import IndexView, BookDetailView, GenreView, AddBookView
    
    app_name = 'books'
    
    urlpatterns = [
        path('', IndexView.as_view(), name='ex2'),
        path('add/', AddBookView.as_view(), name='add'),
        path('g/<str:genre>', GenreView.as_view(), name='genre'),
        path('<slug:slug>/', BookDetailView.as_view(), name='book-detail'),
    ]
##### Views.py

    from django.views.generic.base import TemplateView 
    from django.views.generic.detail import DetailView
    from django.views.generic.list import ListView
    from django.views.generic.edit import FormView, CreateView
    from books.models import Books
    from .forms import AddForm
    from django.db.models import F
    from django.utils import timezone
    
    """
    class AddBookView(FormView):

        template_name = 'add.html'
        form_class = AddForm
        success_url = '/books/'

        def form_valid(self, form):
            form.save()
            return super().form_valid(form)
    """

    class AddBookView(CreateView):
        
        model = Books
        # fields = ['title'] # you can include fields with CreateView as attributes if you want, although it might not be recommended due to visual impacts to the code
        form_class = AddForm # form_class isnt required if you use fields, as it will build in the fields for the form for you
        template_name = 'add.html'
        success_url = '/books/'

        def get_initial(self, *args, **kwargs): ## This funciton can be used to add additional initial information for the view if desired. This would cause Enter Title to appear as text in the box field in the view for Title field.
            initial = super().get_initial(**kwargs)
            initial['title'] = 'Enter Title'
            return initial


    class IndexView(ListView):
        
        model = Books
        template_name = "home.html" # if you use {% for book in object_list %} that wil laod all the books in the template
        context_object_name = 'books' # if you use {% for book in books %} that will load all the books the same as above in the template.
        paginate_by = 4 # this setting allows you to configure how many objects will load per page.
        # queryset = Books.objects.all()[:2] # this tells django that you only want to see 2. Evn though there are 4 of them, it iwll only show you 2.

        def get_queryset(self): # These two lines does the exact same thing that the queryset above does.
            return Books.objects.all()[:2]

    class BookDetailView(DetailView):
        
        model = Books
        template_name = "book-detail.html" ## Note that if you dont stipulate what template to use, Django will by default attempt to define one for one, as in it will decide what it thinks the name should be for the template, and attempt to find it.
        context_object_name = 'book'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            
            post = Books.objects.filter(slug=self.kwargs.get('slug'))
            post.update(count=F('count') + 1)

            context['time] = timezone.now()

            return context

    class GenreView(ListView):

        model = Books
        template_name = 'home.html'
        context_object_name = 'book'
        paginate_by = 2 # Pagination Over-ride

        def get_queryset(self, *args, **kwargs): # These two lines does the exact same thing that the queryset above does.
            return Books.objects.filter(genre__icontains=self.kwargs.get('genre'))

##### Forms.py
    from django import forms
    from .models import Books
    
    class Addform(forms.ModelForm):
    
        class Meta:
            model = Books
            fields = ('title', 'genre', 'author', 'isbn')
    
            widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'genre': forms.TextInput(attrs={'class': 'form-control'}),
                'author': forms.TextInput(attrs={'class': 'form-control'}),
                'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            }
##### add.html

    {% extends "base.html" %}
    {% block content %}
    <div class="container" style="max-width:600px">
      <div class="px-2 py-3 pt-md-5 pb-md-4 mx-auto text-center">
        <h1 class="display-4">All Books</h1>
        <p class="lead"> A range of wonderful programming books to help you learn Javascript.</p>
      </div>
      <div class="py-5">
        <div class="row">
          <div class="col-12">
            <form method="post">
              {% csrf_token %}
              {{ form.as_p }} ### This will wrap everything in a p tag
              <input type="submit">
            </form>
          </div>
        </div>
      </div>
    </div>
    {% endblock %}


### UpdateView
***
CreateView vs UpdateView
They both inherit the same methods & mixins
CreateView
- edit.BaseCreateView
- detail.SingleObjectTemplateResponseMixin
- edit.ModelFormMixin
- detail.SingleObjectMixin
- base.TemplateResponseMixin
- edit.FormMixin
- edit.ProcessFormView
- base.View

UpdateView
- edit.BaseCreateView
- detail.SingleObjectTemplateResponseMixin
- edit.ModelFormMixin
- detail.SingleObjectMixin
- base.TemplateResponseMixin
- edit.FormMixin
- edit.ProcessFormView
- base.View

Whats the Difference?
CreateView
- adds new object/data to a database table
UpdateView
- Retrive specific object/data
- Add/Update the database


##### Models.py

    from django.db import models
    from django.template.defaultfilters import slugify
    
    class Books(models.Model):
        # Example Model Only
        title = models.CharField(max_length=100)
        slug = models.SlugField(null=True)
        genre = models.CharField(max_length=100)
        author = models.CharField(max_length=100)
        isbn = models.CharField(max_length=100)
        count = models.IntegerField(null=True, default=0)

        def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = slugify(self.title)
            return super().save(*args, **kwargs)



##### Urls.py
    from django.urls import path
    from .views import IndexView, BookDetailView, GenreView, AddBookView, BookEditView
    
    app_name = 'books'
    
    urlpatterns = [
        path('', IndexView.as_view(), name='ex2'),
        path('add/', AddBookView.as_view(), name='add'),
        path('g/<str:genre>', GenreView.as_view(), name='genre'),
        path('<slug:slug>/', BookDetailView.as_view(), name='book-detail'),
        path('<slug:slug>/edit', BookEditView.as_view(), name='edit-detail'),
    ]
##### Views.py

    from django.views.generic.base import TemplateView 
    from django.views.generic.detail import DetailView
    from django.views.generic.list import ListView
    from django.views.generic.edit import FormView, CreateView, UpdateView
    from books.models import Books
    from .forms import AddForm
    from django.db.models import F
    from django.utils import timezone
    
    """
    class AddBookView(FormView):

        template_name = 'add.html'
        form_class = AddForm
        success_url = '/books/'

        def form_valid(self, form):
            form.save()
            return super().form_valid(form)
    """
  
    class BookEditView(UpdateView):
        
        model = Books
        # fields = ['title'] # you can include fields with CreateView as attributes if you want, although it might not be recommended due to visual impacts to the code
        form_class = AddForm # form_class isnt required if you use fields, as it will build in the fields for the form for you
        template_name = 'add.html'
        success_url = '/books/'

    class AddBookView(CreateView):
        
        model = Books
        # fields = ['title'] # you can include fields with CreateView as attributes if you want, although it might not be recommended due to visual impacts to the code
        form_class = AddForm # form_class isnt required if you use fields, as it will build in the fields for the form for you
        template_name = 'add.html'
        success_url = '/books/'

        """
        def get_initial(self, *args, **kwargs): ## This funciton can be used to add additional initial information for the view if desired. This would cause Enter Title to appear as text in the box field in the view for Title field.
            initial = super().get_initial(**kwargs)
            initial['title'] = 'Enter Title'
            return initial
        """

    class IndexView(ListView):
        
        model = Books
        template_name = "home.html" # if you use {% for book in object_list %} that wil laod all the books in the template
        context_object_name = 'books' # if you use {% for book in books %} that will load all the books the same as above in the template.
        paginate_by = 4 # this setting allows you to configure how many objects will load per page.
        # queryset = Books.objects.all()[:2] # this tells django that you only want to see 2. Evn though there are 4 of them, it iwll only show you 2.

        def get_queryset(self): # These two lines does the exact same thing that the queryset above does.
            return Books.objects.all()[:2]

    class BookDetailView(DetailView):
        
        model = Books
        template_name = "book-detail.html" ## Note that if you dont stipulate what template to use, Django will by default attempt to define one for one, as in it will decide what it thinks the name should be for the template, and attempt to find it.
        context_object_name = 'book'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            
            post = Books.objects.filter(slug=self.kwargs.get('slug'))
            post.update(count=F('count') + 1)

            context['time] = timezone.now()

            return context

    class GenreView(ListView):

        model = Books
        template_name = 'home.html'
        context_object_name = 'book'
        paginate_by = 2 # Pagination Over-ride

        def get_queryset(self, *args, **kwargs): # These two lines does the exact same thing that the queryset above does.
            return Books.objects.filter(genre__icontains=self.kwargs.get('genre'))

##### Forms.py
    from django import forms
    from .models import Books
    
    class Addform(forms.ModelForm):
    
        class Meta:
            model = Books
            fields = ('title', 'genre', 'author', 'isbn')
    
            widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'genre': forms.TextInput(attrs={'class': 'form-control'}),
                'author': forms.TextInput(attrs={'class': 'form-control'}),
                'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            }
##### add.html

    {% extends "base.html" %}
    {% block content %}
    <div class="container" style="max-width:600px">
      <div class="px-2 py-3 pt-md-5 pb-md-4 mx-auto text-center">
        <h1 class="display-4">All Books</h1>
        <p class="lead"> A range of wonderful programming books to help you learn Javascript.</p>
      </div>
      <div class="py-5">
        <div class="row">
          <div class="col-12">
            <form method="post">
              {% csrf_token %}
              {{ form.as_p }} ### This will wrap everything in a p tag
              <input type="submit">
            </form>
          </div>
        </div>
      </div>
    </div>
    {% endblock %}


---
Sources
-----------

Video Sources
------------


| Component     | Description                                         | Link                                                                                        |
|---------------|-----------------------------------------------------|---------------------------------------------------------------------------------------------|
| TemplateViews | Static Pages or GET Requests                        | [Link](https://www.youtube.com/watch?v=GxA2I-n8NR8) |
| RedirectViews | Redirects to a given URL                            | [Link](https://www.youtube.com/watch?v=ScteNE1jB4g)                                                                            |
| DetailViews   | Present detail of a single model instance           | [Link](https://www.youtube.com/watch?v=dXkmPAnqnTE&list=PLOLrQ9Pn6caxNb9eFZJ6LfY29nZkKmmXT&index=3)                                                                        |
| ListViews     | Present a list of objects                           | [Link](https://www.youtube.com/watch?v=dHvcioGHg08&list=PLOLrQ9Pn6caxNb9eFZJ6LfY29nZkKmmXT&index=4)                                                                          |
| FormViews     | Displaying a Form. Best used for message/emails/EDA | [Link](https://www.youtube.com/watch?v=HX9K6iOjhvI&list=PLOLrQ9Pn6caxNb9eFZJ6LfY29nZkKmmXT&index=5)                                                                          |
| CreateViews   | Displaying a Form. Best used to create objects      | [Link](https://www.youtube.com/watch?v=nW-srV0kKKk&list=PLOLrQ9Pn6caxNb9eFZJ6LfY29nZkKmmXT&index=6)                                                                        |
| UpdateViews   | Best used for adding/updating database tables       | [Link](https://www.youtube.com/watch?v=EUUjJdw3EBM&list=PLOLrQ9Pn6caxNb9eFZJ6LfY29nZkKmmXT&index=7)                                                                       |


Web Sources
------------

| Component   | Description | Link                         |
|-------------| ----------- |------------------------------|
| Placeholder | <Placeholder>| [Link](https://<webaddress>) |
| Placeholder | <Placeholder> | [Link](https://<webaddress>) |
| Placeholder | <Placeholder> | [Link](https://<webaddress>) |
| Placeholder | <Placeholder> | [Link](https://<webaddress>) |
| Placeholder | <Placeholder> | [Link](https://<webaddress>) |
| Placeholder | <Placeholder> | [Link](https://<webaddress>) |
| Placeholder | <Placeholder> | [Link](https://<webaddress>) |
| Placeholder | <Placeholder> | [Link](https://<webaddress>) |
| Placeholder | <Placeholder> | [Link](https://<webaddress>) |
| Placeholder | <Placeholder>| [Link](https://<webaddress>) |
| Placeholder | <Placeholder> | [Link](https://<webaddress>) |


# Class Based Views - Permission Checks 
> Used for define user, process, and object permissions

### User Classes
***
- Superusers
- Staff
  - Special attributes set in the DB Field
- Attritubutes of users
  - username
  - password
  - email
  - first_name
  - last_name

- Auth_users table:
  - id: integer
  - password: varchar(128)
  - last_login: datetime
  - is_superuser: bool
  - username: varchar(150)
  - last_name: varchar(150)
  - email: varchar(254)
  - is_staff: bool
  - is_active: bool
  - date_joined: datetime
  - firstname: varchar(150)

- Adding new users
  - Django built in authentication
    - add new users (not set to Staff or Superusers)
  - By default - if no permissinons are set
    - any new user:
      - add, change, delete, and view any model

django.contrib.auth
- Default model permissions: 
  - add, change, delete, view
- We can use these permissinos to:
  - Apply permission checks
    - Per individual user
    - Group based

Mixins
- AccessMixin
  - PermissionRequiredMixin

##### Views.py

    from django.views.generic.base import TemplateView 
    from django.views.generic.detail import DetailView
    from django.views.generic.list import ListView
    from django.views.generic.edit import FormView, CreateView, UpdateView
    from books.models import Books
    from .forms import AddForm
    from django.db.models import F
    from django.utils import timezone
    # from django.contrib.auth.decorators import permission_required
    from django.contrib.auth.mixins import PermissionRequiredMixin

  
    class BookEditView(PermissionRequiredMixin, UpdateView):
        
        permission_required = 'books.change_books'
        # permission_required = 'books.add_books'
        # permission_required = 'books.delete_books'
        # permission_required = 'books.view_books'
        # permission_required = 'books.view_books', 'books.add_books')   ## You can add as many as you want with the use of a comma.
        
        raise_exception = False   ## True shows the 403 Forbidden message, which is defaultw hen logged in, sends user to login page when logged out
        permission_denied_message = "<custom mesage goes here>"
        login_url = '/books/'   ## This will change the default login auth point url
        redirect_field_name = 'next'   ## This is what shows in the URL. e.g. url/?next=...


        model = Books
        # fields = ['title'] # you can include fields with CreateView as attributes if you want, although it might not be recommended due to visual impacts to the code
        form_class = AddForm # form_class isnt required if you use fields, as it will build in the fields for the form for you
        template_name = 'add.html'
        success_url = '/books/'


##### Views.py

    from django.views.generic.base import TemplateView 
    from django.views.generic.detail import DetailView
    from django.views.generic.list import ListView
    from django.views.generic.edit import FormView, CreateView, UpdateView
    from books.models import Books
    from .forms import AddForm
    from django.db.models import F
    from django.utils import timezone
    # from django.contrib.auth.decorators import permission_required
    from django.contrib.auth.mixins import PermissionRequiredMixin


    class UserAccessMixin(PermissionRequiredMixin):
        def dispath(self, request, *args, **kwargs):
            if (not self.request.user.is_authenticated):
                return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
            if not self.has_permission():
                return redirect('/books')
            return super(UserAccessMixin, self).dispath(request, *args, **kwargs)


    class BookEditView(UserAccessMixin, UpdateView):
        
        permission_required = 'books.change_books'
        # permission_required = 'books.add_books'
        # permission_required = 'books.delete_books'
        # permission_required = 'books.view_books'
        
        raise_exception = False   ## True shows the 403 Forbidden message, which is defaultw hen logged in, sends user to login page when logged out
        permission_denied_message = "<custom mesage goes here>"
        login_url = '/books/'   ## This will change the default login auth point url
        redirect_field_name = 'next'   ## This is what shows in the URL. e.g. url/?next=...


        model = Books
        # fields = ['title'] # you can include fields with CreateView as attributes if you want, although it might not be recommended due to visual impacts to the code
        form_class = AddForm # form_class isnt required if you use fields, as it will build in the fields for the form for you
        template_name = 'add.html'
        success_url = '/books/'


Video Sources
------------

| Component                     | Description                                       | Link                                                                                                |
|-------------------------------|---------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| Class Based Permission Checks | Class Based User, Object, and Process Permissions | [Link](https://www.youtube.com/watch?v=zszYgUXnId8&list=PLOLrQ9Pn6caxNb9eFZJ6LfY29nZkKmmXT&index=8) |
| Placeholder                   | <placeholder>                                     | [Link](https://<website>)                                                                           |
| Placeholder                   | <placeholder>                                     | [Link](https://<website>)                                                                           |
| Placeholder                   | <placeholder>                                     | [Link](https://<website>)                                                                           |
| Placeholder                   | <placeholder>                                     | [Link](https://<website>)                                                                           |
| Placeholder                   | <placeholder>                                     | [Link](https://<website>)                                                                           |
| Placeholder                   | <placeholder>                                     | [Link](https://<website>)                                                                           |


Web Sources
------------

| Component   | Description    | Link                         |
|-------------|----------------|------------------------------|
| Placeholder | <Placeholder>  | [Link](https://<webaddress>) |
| Placeholder | <Placeholder>  | [Link](https://<webaddress>) |
| Placeholder | <Placeholder>  | [Link](https://<webaddress>) |
| Placeholder | <Placeholder>  | [Link](https://<webaddress>) |
| Placeholder | <Placeholder>  | [Link](https://<webaddress>) |
| Placeholder | <Placeholder>  | [Link](https://<webaddress>) |
| Placeholder | <Placeholder>  | [Link](https://<webaddress>) |
| Placeholder | <Placeholder>  | [Link](https://<webaddress>) |
| Placeholder | <Placeholder>  | [Link](https://<webaddress>) |
| Placeholder | <Placeholder>  | [Link](https://<webaddress>) |
| Placeholder | <Placeholder>  | [Link](https://<webaddress>) |



# Function Based Views (FBVs) 
> Text place holder

# CBVs vs FBVs
> Text place holder

# Mixins Basics
> Text place holder
---
---



## [↑](#-table-of-contents) Controllers
> Controllers Notes for Django

---
### Overview
- <additional notes here>
---

| Component   | Description | Link |
| ----------- | ----------- | ----------- |
| Controllers Basics   | Understanding Controllers Basics | [Link](https://<webaddress>) |


---
---

## [↑](#-table-of-contents) URLs
> URLs Notes for Django

---
### Overview 
- <additional notes here>
---

| Component   | Description | Link |
| ----------- | ----------- | ----------- |
| URLs Basics   | Understanding URLs Basics | [Link](https://<webaddress>) |


---
---
## [↑](#-table-of-contents) Databases
> Databases Notes for Django

---
### Overview 
- <additional notes here>
---

| Component                 | Description                           | Link |
|---------------------------|---------------------------------------| ----------- |
| Databases Basics          | Understanding Database Basics         | [Link](https://<webaddress>) |
| Multiple Databases Basics | Understanding Multi-Databases Basics  | [Link](https://<webaddress>) |


Django Multiple Database Configurations


-- Source Video: https://www.youtube.com/watch?v=g-FCzzzjBWo&list=RDCMUC1mxuk7tuQT2D0qTMgKji3w&index=10
-- Source Code: https://github.com/veryacademy/Django-ORM-Mastery-DJ003/tree/main/022-Multiple-Database-Configuration


 Django uses django project settings.py file to dictate what database to uses
 -- when a django app has more than one data, it has to use a router in order to know which database to use.
	-- That configuration typically manifests as:
		-- Author.objects.using('other').all()

		
## Default Database configuration for Django:


DATABASES = {
		'default': {
				'ENGINE': 'django.db.backends.sqlite3',
				'NAME': BASE_DIR / 'db.sqlite3',
		}
}


## End of Configuration ##


## Advanced Database Configuration for Django Example:

DATABASES = {
		'default': {},
		'users_db': {
				'ENGINE': 'django.db.backends.sqlite3',
				'NAME': BASE_DIR / 'users.db.sqlite3',
		},
		'blue_db': {
				'ENGINE': 'django.db.backends.sqlite3',
				'NAME': BASE_DIR / 'blue.db.sqlite3',
		},
}


## End of Configuration
 

Django by default will look for the 'default' database. Without a router configuration within the settings.py file, django
will be unable to find any other databases, even if they are configured. 


-- Create a folder called routers
-- Inside of routers folder, create a file called db_routers.py



## db_routers.py

class AuthRouter:
	# route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin'}  ## Apps that will be using this router, and can migrate to this database
	route_app_labels = {'auth', 'contenttypes'}
	
	## Allows for up to 4 Methods, as seen here
	
	def db_for_read(self, model, **hints):
		if model._meta.app_label in self.route_app_labels:
			return 'users_db'
		return None
		
	def db_for_write(self, model, **hints):
		if model._meta.app_label in self.route_app_labels:
			return 'users_db'
		return None

	def allow_relation(self, obj1, obj2, **hints):
		if (
			obj1._meta.app_label in self.route_app_labels or
			obj2._meta.app_label in self.route_app_labels
		):
			return True
		return None

	def allow_migrate(self,db, app_label, model_name=None, **hints):
		if app_lable in self.route_app_labels:
			return db == 'users_db"
		return None

## End of Configuration



-- Configure Django to use Database Routers

## Settings.py

...

DATABASE_ROUTERS = ['routers.db_routers.AuthRouter',]		

...

## End of Configuration


Once you have the new database declared, configured in settings.py, the routers placed in routers folder in db_routeres.py,
you can then run python manage.py makemigrations | migrate in order to make the migrations.

If there is an issue with a database, such as default is blank, you can do the following:

-- python manage.py makemigrations --database=<specific database>
-- python manage.py migrate --database=<specific database>

** Special Note: Fastest way to find out what apps are using what models is to check in the django content type table

 
 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#			Comprehensive Advanced Configuration of Multiple Databases:
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 
 ## Settings.py
 
 
 ...

DATABASES = {
		'default': {},
		'users_db': {
				'ENGINE': 'django.db.backends.sqlite3',
				'NAME': BASE_DIR / 'users.db.sqlite3',
		},
		'blue_db': {
				'ENGINE': 'django.db.backends.sqlite3',
				'NAME': BASE_DIR / 'blue.db.sqlite3',
		},
		'aqua_db': {
				'ENGINE': 'django.db.backends.sqlite3',
				'NAME': BASE_DIR / 'aqua.db.sqlite3',
		},
}


...

DATABASE_ROUTERS = ['routers.db_routers.AuthRouter', 'routers.db_routers.Blue', 'routers.db_routers.Aqua']		


## db_routers.py


class AuthRouter:
	route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin'}
	
	def db_for_read(self, model, **hints):
		if model._meta.app_label in self.route_app_labels:
			return 'users_db'
		return None
		
	def db_for_write(self, model, **hints):
		if model._meta.app_label in self.route_app_labels:
			return 'users_db'
		return None

	def allow_relation(self, obj1, obj2, **hints):
		if (
			obj1._meta.app_label in self.route_app_labels or
			obj2._meta.app_label in self.route_app_labels
		):
			return True
		return None

	def allow_migrate(self,db, app_label, model_name=None, **hints):
		if app_lable in self.route_app_labels:
			return db == 'users_db'
		return None


class Blue:
	route_app_labels = {'blue'}
	
	def db_for_read(self, model, **hints):
		if model._meta.app_label in self.route_app_labels:
			return 'blue_db'
		return None
		
	def db_for_write(self, model, **hints):
		if model._meta.app_label in self.route_app_labels:
			return 'blue_db'
		return None

	def allow_migrate(self,db, app_label, model_name=None, **hints):
		if app_lable in self.route_app_labels:
			return db == 'blue_db'
		return None


class Aqua:
	route_app_labels = {'aqua'}
		
	def db_for_read(self, model, **hints):
		if model._meta.app_label in self.route_app_labels:
			return 'aqua_db'
		return None
		
	def db_for_write(self, model, **hints):
		if model._meta.app_label in self.route_app_labels:
			return 'aqua_db'
		return None

	def allow_migrate(self,db, app_label, model_name=None, **hints):
		if app_lable in self.route_app_labels:
			return db == 'aqua_db'
		return None


## blue/views.py

from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Blue
from aqua.models import Aqua
from django.http import HttpResponseRedirect


def viewdata(request):
    data = Blue.objects.using('blue_db').all()
    return render(request, "view.html", {"data": data})

class Add(CreateView):
  model = Aqua
  fields = ('title','content','app_name' )
  template_name = 'add.html'
  success_url = '/blue/'

  def form_valid(self, form):
      self.object = form.save(commit=False)
      self.object.save()
      return HttpResponseRedirect(self.get_success_url())


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#										End on Configuration
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

---
---

## [↑](#-table-of-contents) Settings
> Settings Notes for Django

---
### Overview 
- <additional notes here>
---

| Component   | Description | Link |
| ----------- | ----------- | ----------- |
| Views Basics   | Understanding Views Basics | [Link](https://<webaddress>) |


---
---

## [↑](#-table-of-contents) Middleware
> Settings Notes for Django

---
### Overview 
- <additional notes here>
---

| Component         | Description                     | Link |
|-------------------|---------------------------------| ----------- |
| Middleware Basics | Understanding Middleware Basics | [Link](https://<webaddress>) |

Django Middleware


-- Source Video: https://www.youtube.com/watch?v=EpZOVmEw9Qg
-- Source Code: https://github.com/veryacademy/YT_Django_Core_Middleware_Intro


- Described as a framework of hooks into Django's Request/response processing. 
Its a light, low-lvel "plugin" system for globally altering Django's input or Output. 

- Use cases
-- Filtering Requests
-- Injecting Data into Requets/Reponse
-- Performing Logging / Page Analytics

- Django Middleware Hooks
-- Django middleware class has two required methods:
	-- __init__
	-- __call__
	
-- Three optional methods that execute at different points of the view request/reponse life-cycle

-- Called DURING REQUEST:
	-- process_request(request)
	-- process_view(request, view_func, view_args, view_kwargs)
	
-- Called DURING RESPONSE:
	-- process_exception(request, exception)
		- only if the view raised an exception
	-- process_template_response(re quest, response)
		- only if template responses
	-- process_response(request, response)
	

---
---

## [↑](#-table-of-contents) Secure Coding
> Secure Coding Notes for Django

---
### Overview 
- <additional notes here>
---

| Component   | Description | Link |
| ----------- | ----------- | ----------- |
| Secure Coding Basics   | Understanding Secure Coding Basics | [Link](https://<webaddress>) |


---
---

## [↑](#-table-of-contents) Django Unit Tests
> Django Unit Tests Notes for Django

---
### Overview 
- <additional notes here>
---

| Component   | Description | Link |
| ----------- | ----------- | ----------- |
| Django Unit Tests Basics   | Understanding Django Unit Tests Basics | [Link](https://<webaddress>) |


---
---  
  
## [↑](#-table-of-contents) Dockerizing Django
> Dockerizing Django Notes for Django

---
### Overview 
- <additional notes here>
---

| Component   | Description | Link |
| ----------- | ----------- | ----------- |
| Dockerizing Django Basics   | Understanding Dockerizing Django Basics | [Link](https://<webaddress>) |


---
---  
  
## [↑](#-table-of-contents) Deploying to Production
> Deploying to Production Notes for Django

---
### Overview 
- <additional notes here>
---

| Component   | Description | Link |
| ----------- | ----------- | ----------- |
| Deploying to Production Basics   | Understanding Deploying to Production Basics | [Link](https://<webaddress>) |


---
---  


---
---

-  [Link](https://medium.com/@ksarthak4ever/django-class-based-views-vs-function-based-view-e74b47b2e41b)
-  [Link](https://levelup.gitconnected.com/django-celery-going-deeper-with-background-tasks-in-python-fa44958cf7cd)
-  [Link](https://articles.wesionary.team/django-optimizations-database-4945cebb945c)
-  [Link](https://nishanthmurugananth.medium.com/django-user-registration-with-email-verification-a83fd23ef560)
-  [Link](https://medium.com/geekculture/how-to-create-a-saas-web-application-part-1-htmx-django-809b7435b31a)
-  [Link](https://medium.com/geekculture/7-useful-python-libraries-you-should-use-in-your-next-project-538547811de6)
-  [Link](https://dev.to/sirneij/making-django-global-settings-dynamic-the-singleton-design-pattern-25en)
-  [Link](https://www.geeksforgeeks.org/django-templates/)
-  [Link](https://docs.djangoproject.com/en/4.1/topics/auth/default/#topic-authorization)
  
  ## Working with Google Spreadsheets
-  [Link](https://dev.to/sirneij/django-and-google-spreadsheet-api-automatically-creating-and-deleting-multiple-tabs-or-sheets-3hi0)
  
  
  ## Reporting
-  [Link](https://django-slick-reporting.readthedocs.io/en/latest/) Django Slick Reporting with Time Series, Charting, Etc **
-  [Link](https://www.airplane.dev/blog/django-admin-crash-course-how-to-build-a-basic-admin-panel)
-  [Link](https://www.freecodecamp.org/news/how-to-create-an-analytics-dashboard-in-django-app/)
-  [Link](https://www.codementor.io/@chirilovadrian360/django-template-how-to-code-dynamic-pages-in-django-1iqi8vswvx)
-  [Link](https://studygyaan.com/django/how-to-render-dynamic-data-in-django-template)
-  [Link](https://testdriven.io/blog/django-charts/) Adding Charts to Django with Charts.JS
-  [Link](https://studygyaan.com/django/how-to-use-chart-js-in-django) How to use Charts.JS in Django  
-  [Link](https://stackoverflow.com/questions/55983973/how-to-create-dynamic-charts-with-django-and-chart-js) Dynamic Charts with Django, Chart.JS, and AJAX **
-  [Link](https://www.reportbro.com/demo/invoice)
-  [Link](https://docs.reportlab.com/) ReportLab Docs
-  [Link](https://blog.testproject.io/2019/07/16/create-pytest-html-test-reports/) Create PyTest HTML Test Reporting
  

## Custom PDFs

- [Link](https://ordinarycoders.com/blog/article/generating-pdf-with-django) Generating PDFs with Django
- [Link](https://www.youtube.com/watch?v=1x_ACMFzGYM) Generate PDF Reports Dynamically using ReportLab  

## Pivot Tables & Charts
  
- Angular, DevExtreme HTML5 PivotGrid, FlexMonster PivotGrid & Charts, etc [Link](https://medium.com/quick-code/creating-advanced-visual-reports-with-angular-750a1858f194) 
  

-  [Link](https://www.appsloveworld.com/django/100/7/large-django-application-layout)
-  [Link](https://django-report-builder.readthedocs.io/en/latest/quickstart/)
-  [Link](https://www.caktusgroup.com/blog/2018/05/07/creating-dynamic-forms-django/)
-  [Link](https://djangopackages.org/grids/g/reporting/)
-  [Link](https://wkhtmltopdf.org/)
-  [Link](https://github.com/surya-thakur15/Dynamic-Report-Generation-Using-Python-and-MySQL)
-  [Link](https://www.udemy.com/course/creating-a-dynamic-website-with-django-and-python/)
