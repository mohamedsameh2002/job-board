from django.shortcuts import render,redirect
from job.models import Apply
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
@login_required
def send_masseg(request):

    return render (request,'contact/contact.html',{})

@login_required
def applys (request):
    applys=Apply.objects.filter(owner_job = request.user)
    return render (request,'contact/applys.html',{'applys':applys})

def apply_details (request,slug):
    apply_details=Apply.objects.get(slug=slug)
    return render (request,'contact/apply_details.html',{'apply_details':apply_details})

def cv (request,slug):
    cv=Apply.objects.get(slug=slug)
    return render (request,'contact/cv.html',{'cv':cv})
    

def delete_apply (request,slug):
    apply_delet=Apply.objects.get(slug=slug)
    if request.method == 'POST':
        apply_delet.delete()
        return redirect('applys')

    return render (request,'contact/delete_apply.html',{'delete':apply_delet})

    



