from django.shortcuts import render,redirect
from .models import Todo
from django.utils import timezone
from django .http import HttpResponseRedirect

# Create your views here.
def index(request):
    todo_items=Todo.objects.all()
    return render(request,'base.html',{'todo_item':todo_items})

def todo(request):
    current_date=timezone.now()
    content=request.POST['content']
    created_object=Todo.objects.create(added_date=current_date,text=content)
    return redirect('/index')

def delete_todo(request,id):
    Todo.objects.get(pk=id).delete()
    return HttpResponseRedirect('/index')
