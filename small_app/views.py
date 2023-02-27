from django.shortcuts import render , redirect
from .models import Calc
from django.contrib.auth.models import User
from django.views.generic.list import  ListView
from django.views.generic.detail import  DetailView
from django.views.generic.edit import  CreateView , UpdateView , DeleteView , FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy

# Create your views here.

class TaskList(LoginRequiredMixin,ListView):
    model = Calc
    template_name = 'index.html'
    context_object_name = 'tasks'
    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        context['count'] = context['tasks'].filter(completed = False).count()
        search_input = self.request.GET.get('search') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)
            
        context['search_input'] = search_input
        return context

class TaskDetail(LoginRequiredMixin,DetailView):
    model = Calc
    template_name = 'detail.html'
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin,CreateView):
    model = Calc
    fields = ['title', 'description', 'completed']
    template_name = 'add.html'
    success_url = reverse_lazy('calcs:tasks')
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate (LoginRequiredMixin,UpdateView):
    model = Calc
    template_name = "update.html"
    fields =  ['title', 'description', 'completed']
    success_url = reverse_lazy('calcs:tasks')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Calc
    context_object_name = 'task'
    success_url = reverse_lazy('calcs:tasks')
    template_name = 'delete.html'

class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('calcs:tasks')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request , user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args , **kwargs):
        if self.request.user.is_authenticated:
            return redirect('calcs:tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


class CustomLoginView (LoginView):
    template_name = 'login.html'
    fields = "__all__"
    redirect_authenticated_user = True
    
    def get_success_url(self) -> str:
        return reverse_lazy('calcs:tasks')
    

    
    