from django.shortcuts import render,redirect
from .form import SinupForm
from django.contrib.auth import authenticate,login
from .models import *
from .form import UserForm,ProfileForm
from django.urls import reverse

# Create your views here.
#=======================================================
def sinup (request):
    if request.method =='POST':
        form=SinupForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('profile')
            
    else:
        form=SinupForm()

    context={'Sform':SinupForm}
    return render(request,'registration/sinup.html',context)

#==================================================================
def profile (request):
    profile=Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile})

#=================================================================
def profile_edit(request):
    profile=Profile.objects.get(user=request.user)
    if request.method =='POST':
        userForm=UserForm(request.POST,instance=request.user)
        profileForm=ProfileForm(request.POST,request.FILES,instance=profile)
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            myprfile=profileForm.save(commit=False)
            myprfile.user=request.user
            myprfile.save()
            return redirect('profile')
    else:
        userForm=UserForm(instance=request.user)
        profileForm=ProfileForm(instance=profile)
        
    return render(request,'accounts/profile_edit.html',{'Uform':userForm,'Pform':profileForm})
