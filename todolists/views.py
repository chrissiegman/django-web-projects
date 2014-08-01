from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponseRedirect

from todolists.models import ToDoList, ListItem

# Create your views here.

def index(request):
    incomplete_todolist_list = ToDoList.objects.filter(is_complete=False)
    completed_todolist_list = ToDoList.objects.filter(is_complete=True)
    context = {'incomplete_todolist_list': incomplete_todolist_list,
               'completed_todolist_list': completed_todolist_list}
    return render(request, 'todolists/index.html', context)


def detail(request, todolist_id):
    todolist = get_object_or_404(ToDoList, pk=todolist_id)
    incomplete_listitem_list = ListItem.objects.filter(todolist_id=todolist_id, is_complete=False)
    completed_listitem_list = ListItem.objects.filter(todolist_id=todolist_id, is_complete=True)
    context = {'incomplete_listitem_list': incomplete_listitem_list,
               'completed_listitem_list': completed_listitem_list,
               'todolist': todolist,
               }
    return render(request, 'todolists/detail.html', context)

def toggle_completion(request, todolist_id):
    todolist = get_object_or_404(ToDoList, pk=todolist_id)
    selected_item = todolist.listitem_set.get(pk=request.POST['listitem'])
    
    if selected_item.is_complete == False:
        selected_item.is_complete = True
    elif selected_item.is_complete == True:
        selected_item.is_complete = False
    selected_item.save()
    return HttpResponseRedirect(reverse('todolists:detail', args=(todolist.id,)))

