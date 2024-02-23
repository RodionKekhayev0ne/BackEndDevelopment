from django.shortcuts import render, redirect
from .form import CUForm
from .models import Todo


# Create your views here.
def main(request):

    todo = Todo.objects.all()
    context = {'todo':todo}
    return render(request, 'main.html', context)


def createAction(request):
    form = CUForm()
    context = {'form': form}
    return render(request, 'form.html', context)


def updateAction(request, pk):
    form = CUForm()
    todo = Todo.objects.get(pk=id)
    context = {'form': form, 'todo': todo}
    return render(request, 'update.html', context)


def create(request):
    form = CUForm(request.POST)
    if form.is_valid():
        todo = Todo()
        todo.title = form.cleaned_data['title']
        todo.description = form.cleaned_data['description']
        todo.due_date = form.cleaned_data['due_date']
        todo.isDone = False
        todo.save()
        print("Created TODO")
    return redirect("/")


def update(request, pk):
    form = CUForm(request.POST)
    todo = Todo.objects.get(pk=id)
    todo.title = form.title
    todo.description = form.description
    todo.due_date = form.due_date
    Todo.save(todo)

    return render(request, "main.html")
