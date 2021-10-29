from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TodoForm
from .models import TodoList

# Create your views here.


def todo(request):
    if request.method == 'GET':
        tasks = TodoList.objects.all().order_by('-task_id')
        form = TodoForm()
        return render(request=request, template_name='list.html', context={'tasks': tasks, 'form': form})

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            # add new task to TodoList database
            TodoList.objects.create(task=task)
        return HttpResponseRedirect(reverse('todo'))


def task(request, task_id):
    if request.method == 'GET':
      # look up TodoList object by id
        todo = TodoList.objects.get(pk=task_id)
        # make a form and prepopulate it with the requested task
        form = TodoForm(initial={'task': todo.task})
        return render(request, template_name='detail.html', context={'form': form, 'task_id': task_id})

    if request.method == 'POST':
        if 'save' in request.POST:
            form = TodoForm(request.POST)
            if form.is_valid():
                task = form.cleaned_data['task']
                TodoList.objects.filter(pk=task_id).update(task=task)
        elif 'delete' in request.POST:
            TodoList.objects.filter(pk=task_id).delete()
        return HttpResponseRedirect(reverse('todo'))
