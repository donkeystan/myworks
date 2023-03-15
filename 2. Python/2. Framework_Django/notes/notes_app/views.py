from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from notes_app.models import Note
# Create your views here.

# ----- Login/Logout -----
def index(request):
    if (request.user.is_authenticated):
        name = request.user.username
    return render(request, 'index.html', locals())

def logout(request):
	auth.logout(request)
	return redirect('/login/')

def login(request):
    if (request.user.id == None):
        message = '尚未登入'

    if (request.method == 'POST'):
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=name, password=password)
        if (user is not None):
            if (user.is_active):
                auth.login(request,user)
                print(f'user id {user.id}')
                return redirect('/notes/')
                message = '登入成功！'
            else:
                message = '帳號尚未啟用！'
        else:
            message = '登入失敗！'
    return render(request, 'login.html', locals())

# ----- Notes Main Page  -----
def notes(request):
    if (request.user.id == None):
        return redirect('/login/')

    username = request.user.username
    curr_user_id = request.user.id
    notes = Note.objects.filter(UserID=curr_user_id).order_by('-DateOfCreate')
    notes = notes.filter(Archived='False')
    if (request.method == 'POST'):
        title = request.POST['title']
        content = request.POST['content']
        note = Note.objects.create(UserID=curr_user_id, Title=title, Content=content, Archived='False')
        note.save()
        print(f'Note {note.id} saved for --- user {curr_user_id}')
        return redirect('.')
    else:
        message = '歡迎隨手記!'
    context = {'notes':notes, 'message':message, 'username':username}
    return render(request, 'notes.html', context)

def archived(request):
    if (request.user.id == None):
        return redirect('/login/')

    username = request.user.username
    curr_user_id = request.user.id
    notes = Note.objects.filter(UserID=curr_user_id).order_by('-DateOfCreate')
    notes = notes.filter(Archived='True')
    return render(request, 'archived.html', locals())

# ----- Archiving /De-Archiving -----
def archiving(request, id=None):
    if (request.user.id == None):
        return redirect('/login/')

    if (id != None):
        if (request.method == 'POST'):
            id = request.POST['id']
        try:
            note = Note.objects.get(id=id)
            note.Archived = 'True'
            note.save()
            return redirect('/notes')
        except:
            message = '錯誤!'			
    return render(request, 'archiving.html', locals())

def de_archiving(request, id=None):
    if (request.user.id == None):
        return redirect('/login/')

    if (id != None): 
        if (request.method == 'POST'):
            id = request.POST['id']
        try:
            note = Note.objects.get(id=id)
            note.Archived = 'False'
            note.save()
            return redirect('/archived')
        except:
            message = '錯誤!'
    return render(request, 'de_archiving.html', locals())

# ----- Edit -----
def edit(request, id=None, mode=None):
    if (request.user.id == None):
        return redirect('/login/')

    if (mode == 'save'):
        note = Note.objects.get(id=id)
        note.Title = request.POST['title']
        note.Content = request.POST['content']
        note.save()
        return redirect('/notes')
    else:
        username = request.user.username
        curr_user_id = request.user.id
        notes = Note.objects.filter(UserID=curr_user_id).order_by('-DateOfCreate')
        notes = notes.filter(Archived='False')
        current_id = id
        message = '修改模式，請輸入修改標題或內容！'
        context = {'notes':notes, 'username':username, 'message':message, 'current_id':current_id}
        return render(request, 'edit.html', context)

# ----- Delete -----
def delete(request, id=None):
    if (request.user.id == None):
        return redirect('/login/')

    if (id != None):
        if (request.method == 'POST'):
            id = request.POST['id']
        try:
            note = Note.objects.get(id=id)  
            note.delete()
            return redirect('/notes')
        except:
            message = '錯誤!'
    return render(request, 'delete.html', locals())	