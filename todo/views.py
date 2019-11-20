from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html',
        {'all_items': all_todo_items})

def addTodo(request):
    TodoItem(content = request.POST['content']).save()
    return HttpResponseRedirect('/')

def deleteTodo(request, todo_id):
    TodoItem.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')

def completeTodo(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.complete = True
    todo.save()
    return HttpResponseRedirect('/')

def aboutView(request):
    return render(request, 'about.html')

def authorsView(request):
    return render(request, 'authors.html')
