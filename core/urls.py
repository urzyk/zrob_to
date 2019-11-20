from django.contrib import admin
from django.urls import path
from todo.views import todoView, addTodo, deleteTodo, aboutView, authorsView, completeTodo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addTodo/', addTodo),
    path('deleteTodo/<int:todo_id>/', deleteTodo),
    path('completeTodo/<int:todo_id>/', completeTodo),
    path('', todoView),
    path('about', aboutView),
    path('authors', authorsView),
]
