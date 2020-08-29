from django.db import models
from django.contrib.auth.models import auth,User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profilepic=models.ImageField(upload_to="Profilepics",default="profilepics/profilepic.jpeg")
    phone=models.CharField(max_length=15,default="NULL",null=True)
    gender=models.CharField(max_length=8,default="male",null=True)
    wins=models.IntegerField(default=0)
    rewards=models.IntegerField(default=0)
    quiz=models.IntegerField(default=0)
    quiztime=models.IntegerField(default=0)
    parquiztime=models.BooleanField(default=False)
    weekendquiz=models.IntegerField(default=0)
    parwkndquiz=models.BooleanField(default=False)
    weeklyquiz=models.IntegerField(default=0)
    parwklyquiz=models.BooleanField(default=False)
