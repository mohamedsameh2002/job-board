from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator
from .form import ApplyForm,JobForm
from django .urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JobtFilter


# Create your views here.

#===================================================
@login_required
def job_list(request):
    job_list=Job.objects.all()
    #filrtes===========
    myfilter=JobtFilter(request.GET,queryset=job_list)
    job_list=myfilter.qs

    paginator=Paginator(job_list,7)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)


    context={"jobs":page_obj,'myfilter':myfilter}
    return render(request,'job/job_list.html',context)

#=========================================================
@login_required
def job_details(request, slug):
    job_details=Job.objects.get(slug=slug)

    if request.method == 'POST':
        form=ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            my_form=form.save(commit=False)
            my_form.job=job_details
            my_form.owner=request.user
            my_form.owner_job=job_details.owner
            my_form=form.save()
            return redirect ('job_list')
    else:
        form=ApplyForm()
    context={"jobs":job_details,'Aform':form}
    return render(request,'job/job_details.html',context)
#========================================================
@login_required
def add_job(request):
    if request.method =='POST':
        form=JobForm(request.POST,request.FILES)
        if form.is_valid:
            my_form=form.save(commit=False)
            my_form.owner=request.user
            my_form=form.save()
            return redirect('job_list')
    else:
        form=JobForm()
    return render(request,'job/add_job.html',{'Jform':form})

#===============================================
@login_required
def edit_job (request,slug):
    file_edit=Job.objects.get(slug=slug)
    if request.method == "POST":
        edit_form=JobForm(request.POST,request.FILES,instance=file_edit)
        if edit_form.is_valid():
            myfile=edit_form.save(commit=False)
            myfile.user=request.user
            myfile.save()
            return redirect('job_list')
    else:
        edit_form=JobForm(instance=file_edit)

    return render (request,'job/edit.html',{'edform':edit_form})
#=========================================
def delet_job (request,slug):
    delet=Job.objects.get(slug=slug)
    if request.method == 'POST':
        delet.delete()
        return redirect('job_list')
    return render (request,'job/delete.html',{'delete':delet})
