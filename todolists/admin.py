from django.contrib import admin

from todolists.models import ToDoList, ListItem

class ListItemInline(admin.TabularInline):
    model = ListItem
    extra = 5

class ToDoListAdmin(admin.ModelAdmin):
    fieldsets = [
            ('To Do List', {'fields': ['list_name']}),
            ('Date information', {'fields': ['pub_date']}),
            ]
    inlines = [ListItemInline]
    list_display = ('list_name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question']

# Register your models here.
admin.site.register(ToDoList, ToDoListAdmin)
