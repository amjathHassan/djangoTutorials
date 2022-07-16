from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView, DeleteView, DetailView
from .forms import ContactForm
from .models import Teacher

# Create your views here.

# def homepage(request):
#     return render(request, 'classroom/class_home.html')


class HomeView(TemplateView):
    template_name = 'classroom/class_home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thankyou.html'

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'
    success_url = reverse_lazy('classroom:thank_you')
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class TeacherCreateView(CreateView):
    model = Teacher
    fields = '__all__'
    
    success_url = reverse_lazy('classroom:thank_you')

class TeacherListView(ListView):
    model = Teacher
    queryset = Teacher.objects.order_by('first_name')
    context_object_name = 'object_list'
 
class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = '__all__'
    success_url= reverse_lazy('classroom:list_teacher')

class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('classroom:list_teacher')

class TeacherDetailView(DetailView):
    model = Teacher