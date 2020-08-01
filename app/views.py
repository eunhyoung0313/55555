from django.shortcuts import render,redirect
from .models import Post, Comment, Study
import datetime
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .utils import upload_and_save

# Create your views here.
def index(request):
    return render(request, 'index.html')


#alumni
def alumni(request):
    return render(request, '1-alumni.html')


#session
def session(request):
    if request.method=="POST":
        file_to_upload=request.FILES.get('img')
        upload_and_save(request, file_to_upload)
        return redirect('session')
    posts=Post.objects.all()

    return render(request,'2-session.html',{'posts':posts})

def session_detail(request,post_pk):
    post=Post.objects.get(pk=post_pk)

    if request.method=="POST":
        Comment.objects.create(
            post=post,
            content=request.POST['content'],
            author=request.user
        )
        return redirect('session_detail',post_pk)

    return render(request, 'session_detail.html', {'post':post})

@login_required(login_url='/registration/login')
def session_new(request):
    if request.method=='POST':
        new_post=Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            duedate=request.POST['duedate'],
            author=request.user
        )
        return redirect('session_detail',new_post.pk)
    
    return render(request, 'session_new.html')


#assignment
def assignment(request):
    return render(request, '3-assignment.html')


#contact
def contact(request):
    return render(request, '4-contact.html')


#study
def study(request):
    posts= Study.objects.all()

    return render(request, '4-study.html', {posts: posts})

# @login_required(login_url = '/registration/login')
def study_detail(request,post_pk):
    post=Study.objects.get(pk=post_pk)

    if request.method=="POST":
        Study.objects.create(
            post=post,
            content=request.POST['content'],
            # author=request.user
        )
        return redirect('study_detail',post_pk)

    return render(request, '4-study_detail.html', {'post':post})

def study_new(request):
    if request.method == 'POST':
        new_post = Study.objects.create(
            title= request.POST['title'],
            content = request.POST['content'],
            # author = request.user 
        )
        return redirect('study_detail', new_post.pk)
    return render (request, '4-study_new.html')
#my
def my(request):
    posts=Post.objects.all()
    return render(request,'my.html',{'posts':posts})



def edit(request,post_pk):
    post=Post.objects.get(pk=post_pk)

    if request.method=='POST':
        Post.objects.filter(pk=post_pk).update(
            title=request.POST['title'],
            content=request.POST['content'],
            duedate=request.POST['duedate'],
        )
        return redirect('detail', post_pk)
    
    return render(request, 'edit.html',{'post':post})


def delete(request,post_pk):
    post=Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')

# @login_required(login_url='/registration/login')
def delete_comment(request,post_pk,comment_pk):
    comment=Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', post_pk)

def signup(request):
    if(request.method=="POST"):
        found_user=User.objects.filter(username=request.POST['username'])
        if (len(found_user)>0):
            error='username이 이미 존재합니다'
            return render(request,'registration/signup.html',{'error':error})

        new_user=User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )

        auth.login(
            request,
            new_user,
            backend='django.contrib.auth.backends.ModelBackend'
            )
        return redirect('index')

    return render(request,'registration/signup.html')

def login(request):
    if (request.method=="POST"):
        found_user=auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if (found_user is None):
            error='아이디 또는 비밀번호가 틀렸습니다'
            return render(request,'registration/login.html',{'error':error})

        auth.login(
            request,
            found_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )

        return redirect(request.GET.get('next','/'))
        
    return render(request,'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')