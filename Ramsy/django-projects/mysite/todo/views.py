from django.shortcuts import render
from .models import Note, Todo
from .forms import TodoForm, NoteForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# todo list homepage
def todo(request):
    #if user is asking for a page to be displayed 
    if request.method == 'GET':
        # tasks is our QuerySet of Todo objects 
        tasks = Todo.objects.all().order_by('-task_id')
        # 1 instance of the TodoForm class
        form = TodoForm()
        return render(request=request,
                      template_name = 'list.html',
                      # 'form' is comparing the form from list.html and second form is matching the variable here
                      context = {'tasks':tasks, 'form':form})
    
    # when user submits form
    if request.method == 'POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            # add new Todo object to QuerySet 
            Todo.objects.create(task=task)
        # "redirect" to the todo homepage   
        return HttpResponseRedirect(reverse('todo'))


def task(request, task_id):
    if request.method == 'GET':
        # looking up a specific todo object by the pk(primary key)
        todo = Todo.objects.get(pk=task_id)
        # make a form, pre-populate the character field with the name of the task
        form = TodoForm(initial = {'task':todo.task})
        return render(request = request,
                      template_name = 'detail.html',
                      context = {
                          'form':form,
                          'task_id': task_id
                      })
    
    if request.method == 'POST':
        if 'save' in request.POST:
            form = TodoForm(request.POST)
            if form.is_valid():
                task=form.cleaned_data['task']
                # update task attribute of the task of the correct task_id to match what user inputs
                Todo.objects.filter(pk=task_id).update(task=task)
        elif 'delete' in request.POST:
            Todo.objects.filter(pk=task_id).delete()
        return HttpResponseRedirect(reverse('todo'))


def notes(request):
    #if user is asking for a page to be displayed 
    if request.method == 'GET':
        # tasks is our QuerySet of Todo objects 
        notes = Note.objects.all().order_by('note_id')
        # 1 instance of the TodoForm class
        form = NoteForm()
        return render(request=request,
                      template_name = 'notes.html',
                      # 'form' is comparing the form from list.html and second form is matching the variable here
                      context = {'notes':notes, 'form':form})


        # when user submits form
    if request.method == 'POST':
        form= NoteForm(request.POST)
        if form.is_valid():
            note_text = form.cleaned_data['note_text']
            # add new note object to QuerySet 
            Note.objects.create(note_text=note_text)
        # "redirect" to the todo homepage   
        return HttpResponseRedirect(reverse('notes'))
