from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from .models import Author, Book, BookInstance, Genre, Language
from django.views.generic import CreateView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView

# Create your views here.
def home_page_catalog(request):
    return HttpResponse("RedirectView redirected to catalog")

def index(request):
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_instance_avail = BookInstance.objects.filter(status__exact = 'a').count()

    context = {
        'num_books' : num_books,
        'num_instance': num_instance,
        'num_instance_avail': num_instance_avail,
    }

    return render(request, 'catalog/index.html', context= context)

class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = '__all__'
    
class BookDetail(DetailView):
    model = Book

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'

class AuthorDetail(DetailView):
    model = Author

class GenreCreate(CreateView):
    model = Genre
    fields = '__all__'

class GenreDetail(DetailView):
    model = Genre

class LanguageCreate(CreateView):
    model = Language
    fields = '__all__'

class LanguageDetail(DetailView):
    model = Language

@login_required
def my_view(request):
    return render(request, 'catalog/my_view.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'catalog/signup.html'

class CheckedOutByUserView(LoginRequiredMixin, ListView):
    model = BookInstance
    template_name = 'catalog/profile.html'
    paginate_by = 5
    def get_queryset(self):
        return BookInstance.objects.filter(borrower = self.request.user)