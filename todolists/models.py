from django.db import models
from django.shortcuts import get_object_or_404

# Create your models here.

class ToDoList(models.Model):
    list_name = models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.list_name

class ListItem(models.Model):
    todolist = models.ForeignKey(ToDoList)
    list_item_text = models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False)

    def __unicode__(self):
        return self.list_item_text
