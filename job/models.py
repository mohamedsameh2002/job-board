from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import random

# Create your models here.
JOB_TYPE=[
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
]

def image_upload (instance,filename):
    random_namper=random.randint(0,10000000)
    return f"image-job/ {random_namper}.png"

class Job (models.Model):
    owner=models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    Country= models.CharField(max_length=50)
    jop_type=models.CharField(max_length=20,choices=JOB_TYPE)
    description=models.TextField(max_length=1000,default='')
    Published_at=models.DateField(auto_now=True)
    Vacancy=models.IntegerField(max_length=500,default=1)
    Salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    slug=models.SlugField(null=True,blank=True)

    def save (self,*args,**kwarges):
        self.slug=slugify(self.title)
        super(Job,self).save(*args,**kwarges)
        

    def __str__(self) -> str:
            return self.title


class Category (models.Model):
    name=models.CharField(max_length=25)
    def __str__(self) -> str:
            return self.name

class Apply (models.Model):
    owner=models.ForeignKey(User, related_name='apply_owner', on_delete=models.CASCADE)
    owner_job=models.ForeignKey(User, related_name='owner_job', on_delete=models.CASCADE)
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    website=models.URLField(null=True,blank=True)
    cv=models.FileField(upload_to='apply/')
    cover_letter=models.TextField(max_length=500,null=True,blank=True)
    criated_at=models.DateField(auto_now=True)
    slug=models.SlugField(null=True,blank=True)

    def save (self,*args,**kwarges):
        self.slug=slugify(self.name)
        super(Apply,self).save(*args,**kwarges)
    def __str__(self) -> str:
        return self.name
    
    def __str__(self) -> str:
        return self.name
