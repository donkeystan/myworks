from django.shortcuts import render, redirect
from todo_list_app.forms import PostForm
from todo_list_app.models import Task
from django.http import HttpResponse

################################################## Pages ##################################################
def index(request):
    return HttpResponse('Hello Welcome to ToDoList Site!')

def todo(request):
    todo_tasks = Task.objects.filter(complete="False").order_by('-dateOfCreated')
    done_tasks = Task.objects.filter(complete="True").order_by('-dateOfCreated')
    todo_tasks = todo_tasks.filter(archived="False")
    done_tasks = done_tasks.filter(archived="False")
    if (request.method == "POST"):
        title = request.POST['title']
        taskContent = request.POST['taskContent']
        complete =  request.POST['complete']
        task = Task.objects.create(title=title, taskContent=taskContent, complete=complete)
        task.save()
        return redirect('.')
    else:
        message = '請輸入待辦事項！' 
    context = {'todo_tasks':todo_tasks, 'done_tasks':done_tasks, 'message':message}
    return render(request, 'todo.html', context)

def archived(request):
    tasks = Task.objects.filter(archived="True").order_by('-dateOfCreated')
    return render(request, 'archived.html', locals())

################################################## Delete ##################################################
def delete(request, id=None):
    if (id != None):
        if (request.method == "POST"):
            id = request.POST['id']
        try:
            task = Task.objects.get(id=id)  
            task.delete()
            return redirect('/todo')
        except:
            message = "讀取錯誤!"			
    return render(request, "delete.html", locals())	

################################################## Complete/Incomplete ##################################################
def complete(request, id=None):
    if (id != None):
        if (request.method == "POST"):
            id = request.POST['id']
        try:
            task = Task.objects.get(id=id)
            task.complete = "True"
            task.save()
            return redirect('/todo')
        except:
            message = "讀取錯誤!"			
    return render(request, "complete.html", locals())

def incomplete(request, id=None):
    if (id != None):
        if (request.method == "POST"):
            id = request.POST['id']
        try:
            task = Task.objects.get(id=id)
            task.complete = "False"
            task.save()
            return redirect('/todo')
        except:
            message = "讀取錯誤!"			
    return render(request, "complete.html", locals())


################################################## Archiving /De-Archiving ##################################################
def archiving(request, id=None):
    if (id != None):
        if (request.method == "POST"):
            id = request.POST['id']
        try:
            task = Task.objects.get(id=id)
            task.archived = "True"
            task.save()
            return redirect('/todo')
        except:
            message = "讀取錯誤!"			
    return render(request, "archiving.html", locals())

def de_archiving(request, id=None):
    if (id != None):
        if (request.method == "POST"):
            id = request.POST['id']
        try:
            task = Task.objects.get(id=id)
            task.archived = "False"
            task.save()
            return redirect('/archived')
        except:
            message = "讀取錯誤!"
    return render(request, "de_archiving.html", locals())

################################################## Edit ##################################################
def edit(request, id=None, mode=None):
    if (mode == "save"):
        task = Task.objects.get(id=id)
        task.title = request.POST['title']
        task.taskContent = request.POST['taskContent']
        task.save()
        return redirect('/todo')
    else:
        todo_tasks = Task.objects.filter(complete="False").order_by('-dateOfCreated')
        done_tasks = Task.objects.filter(complete="True").order_by('-dateOfCreated')
        current_id = id
        message = '請輸入待辦事項！'
        context = {'todo_tasks':todo_tasks, 'done_tasks':done_tasks, 'message':message, 'current_id':id}
        return render(request, 'edit.html', context)