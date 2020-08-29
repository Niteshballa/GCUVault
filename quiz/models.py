from django.db import models
from django.contrib.auth.models import auth,User
# Create your models here.
class Quiz(models.Model):
    qname=models.CharField(max_length=200)
    q1=models.CharField(max_length=300)
    q1opt1=models.CharField(max_length=50)
    q1opt2=models.CharField(max_length=50)
    q1opt3=models.CharField(max_length=50)
    q1opt4=models.CharField(max_length=50)
    q2=models.CharField(max_length=300)
    q2opt1=models.CharField(max_length=50)
    q2opt2=models.CharField(max_length=50)
    q2opt3=models.CharField(max_length=50)
    q2opt4=models.CharField(max_length=50)
    q3=models.CharField(max_length=300)
    q3opt1=models.CharField(max_length=50)
    q3opt2=models.CharField(max_length=50)
    q3opt3=models.CharField(max_length=50)
    q3opt4=models.CharField(max_length=50)
    q4=models.CharField(max_length=300)
    q4opt1=models.CharField(max_length=50)
    q4opt2=models.CharField(max_length=50)
    q4opt3=models.CharField(max_length=50)
    q4opt4=models.CharField(max_length=50)
    q5=models.CharField(max_length=300)
    q5opt1=models.CharField(max_length=50)
    q5opt2=models.CharField(max_length=50)
    q5opt3=models.CharField(max_length=50)
    q5opt4=models.CharField(max_length=50)
    q6=models.CharField(max_length=300)
    q6opt1=models.CharField(max_length=50)
    q6opt2=models.CharField(max_length=50)
    q6opt3=models.CharField(max_length=50)
    q6opt4=models.CharField(max_length=50)
    q7=models.CharField(max_length=300)
    q7opt1=models.CharField(max_length=50)
    q7opt2=models.CharField(max_length=50)
    q7opt3=models.CharField(max_length=50)
    q7opt4=models.CharField(max_length=50)
    q8=models.CharField(max_length=300)
    q8opt1=models.CharField(max_length=50)
    q8opt2=models.CharField(max_length=50)
    q8opt3=models.CharField(max_length=50)
    q8opt4=models.CharField(max_length=50)
    q9=models.CharField(max_length=300)
    q9opt1=models.CharField(max_length=50)
    q9opt2=models.CharField(max_length=50)
    q9opt3=models.CharField(max_length=50)
    q9opt4=models.CharField(max_length=50)
    q10=models.CharField(max_length=300)
    q10opt1=models.CharField(max_length=50)
    q10opt2=models.CharField(max_length=50)
    q10opt3=models.CharField(max_length=50)
    q10opt4=models.CharField(max_length=50)
    start=models.DateTimeField()
    end=models.DateTimeField()
    
class answer(models.Model):
    qname=models.CharField(max_length=100)
    q1ans=models.CharField(max_length=50)
    q2ans=models.CharField(max_length=50)
    q3ans=models.CharField(max_length=50)
    q4ans=models.CharField(max_length=50)
    q5ans=models.CharField(max_length=50)
    q6ans=models.CharField(max_length=50)
    q7ans=models.CharField(max_length=50)
    q8ans=models.CharField(max_length=50)
    q9ans=models.CharField(max_length=50)
    q10ans=models.CharField(max_length=50)

class eligible(models.Model):
    username=models.CharField(max_length=100)

class contests(models.Model):
    contestname=models.CharField(max_length=100)
    start=models.DateTimeField()
    end=models.DateTimeField()
    upcoming=models.BooleanField()

class winners(models.Model):
    username=models.CharField(max_length=100)
    isrewarded=models.BooleanField(default=False)
    