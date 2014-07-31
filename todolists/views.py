from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import generic

from todolists.models import ToDoList

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'todolists/index.html'
    context_object_name = 'todolist_list'

    def get_queryset(self):
        return ToDoList.objects.all()

class DetailView(generic.DetailView):
    model = ToDoList
    template_name = 'todolists/detail.html'

