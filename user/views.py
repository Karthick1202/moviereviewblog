# from django.shortcuts import render
# from .forms import RegisterForm
# from django.contrib.auth.hashers import make_password
# from django.contrib.auth.forms import AuthenticationForm
# from django.http import HttpResponse  
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate,login,logout
# # Create your views here.

# def RegisterView(request):
#     form=RegisterForm
#     if request.method=='POST':
#         form=RegisterForm(request.POST)
#         if form.is_valid():
#             form=form.save(commit=False)
#             password=form.password
#             form.password=make_password(password)
#             form.save()
#             return HttpResponse('Register Sucessfully')
#     return render(request,'register.html',{'form':form})


# def loginview(request):
#     form=AuthenticationForm
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user=authenticate(username=username,password=password)
#         if user is not None:
#             login(request,user)
#         else:
#             form=RegisterForm
#             if request.method=='POST':
#                 form=RegisterForm(request.POST)
#                 if form.is_valid():
#                     form=form.save(commit=False)
#                     password=form.password
#                     form.password=make_password(password)
#                     form.save()
#                     return HttpResponse('Register Sucessfully')
#             return render(request,'register.html',{'form':form})
#                     # return render(request,'register.html')
#     return render(request,'login.html',{'form':form})

# @login_required(login_url='/login/')
# def logoutview(request):
#     logout(request)
#     return HttpResponse('logout sucessfull')