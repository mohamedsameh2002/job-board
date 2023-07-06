# logic (views)
from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['GET'])
def jobs_list_api (request):
    all_jobs=Job.objects.all()
    data=JobSerializer(all_jobs,many=True).data
    return Response({'data':data})

@api_view(['GET'])
def job_detal_api (request,id):
    job_detale=Job.objects.get(id=id)
    data=JobSerializer(job_detale).data
    return Response({'data_det':data})



# class based view====(generic)
class JobListApi (generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobDetaleApi (generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class=JobSerializer
    lookup_field='id'