from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import moviereviewform,commentform
from .models import movie,comments
from .forms import RegisterForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def movieview(request):
    form=moviereviewform()
    if request.method=='POST' and request._files:
        form2=moviereviewform(request.POST,request._files)
        if form2.is_valid():
            form2.save()
    return render(request,'movie.html',{'form':form})

def displayall(request):
    data=movie.objects.all()
    return render(request,'home.html',{'data':data})

@login_required(login_url='/login/')
def displayone(request,id):
    data=movie.objects.get(id=id)
    form=commentform(initial={'review':id})
    comment=comments.objects.filter(review_id=id)
    if request.method=='POST':
        form1=commentform(request.POST)
        if form1.is_valid():
            form1.save()
    return render(request,'single.html',{'data':data,'form':form,'comment':comment})

def homepageview(request):
    return render(request,'homepage.html')

def RegisterView(request):
    form=RegisterForm
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            password=form.password
            form.password=make_password(password)
            form.save()
            subject = 'welcome to My MovieBlog'
            message = f'Hi {form.username}, Thank you for registering in my MovieBlog.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [form.email, ]
            send_mail( subject, message, email_from, recipient_list )
            return HttpResponse('Register Sucessfully')
    return render(request,'register.html',{'form':form})


def loginview(request):
    form=AuthenticationForm
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
            # data=movie.objects.all()
            # return render(request,'home.html',{'data':data})
        else:
            form1=RegisterForm
            if request.method=='POST':
                form1=RegisterForm(request.POST)
                if form1.is_valid():
                    form1=form1.save(commit=False)
                    password=form1.password
                    form1.password=make_password(password)
                    form1.save()
                    return HttpResponse('Register Sucessfully')
            return render(request,'register.html',{'form':form1})
                    # return render(request,'register.html')
    return render(request,'login.html',{'form':form})

@login_required(login_url='/login/')
def logoutview(request):
    logout(request)
    return redirect('home')
    































# def commentview(request):
#     form=commentform()
#     if request.method=='POST':
#         form=commentform(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Comment Posted Sucessfully')
#     return render(request,'comment.html',{'form':form})