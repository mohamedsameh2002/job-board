from django.shortcuts import render
from job.models import *



# Create your views here.
def index (request):
    jobs=Job.objects.all()
    context={'jobs':jobs}
    return render(request,'index.html',context)
    
