from django.shortcuts import render, redirect
from .form import CUForm
from .models import Todo


# Create your views here.
def main(request):
    todo = Todo.objects.all()
    context = {'todo': todo}
    return render(request, 'main.html', context)


def createAction(request):
    todo = Todo()
    form = CUForm(request.POST, instance=todo)
    context = {'form': form}
    return render(request, 'form.html', context)


def updateAction(request, pk):
    todo = Todo.objects.get(id=pk)
    form = CUForm(instance=todo)

    return render(request, 'update.html', {'form': form, 'todo': todo})


def create(request):
    todo = Todo()
    form = CUForm(request.POST,instance=todo)
    if form.is_valid():
        todo = Todo()
        todo.title = form.cleaned_data['title']
        todo.description = form.cleaned_data['description']
        todo.due_date = form.cleaned_data['due_date']
        todo.isDone = False
        todo.save()
        print("Created TODO")
    return redirect("/")


def done(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect("/")


def update(request, pk):
    todo = Todo.objects.get(id=pk)

    if request.method == 'POST':

        form = CUForm(request.POST or None, instance=todo)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = CUForm(instance=todo)
    return render(request, '/updateAction/' + pk, {'form': form})
