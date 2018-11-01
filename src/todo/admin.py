from django.contrib import admin
from .models import Task 

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	list_display =('title','description', 'status','due_date')
	list_filter =('status','due_date')
	search_fields=('title',' description')
	ordering=['status','due_date']


