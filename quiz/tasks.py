from __future__  import absolute_import,unicode_literals

from celery.schedules import crontab
from celery.task import periodic_task
 
from quiz.models import Quiz,eligible,winners
from accounts.models import UserProfile
from django.contrib.auth.models import auth,User


from django.core.mail import EmailMessage
from django.template.loader import render_to_string

import random

quiz=Quiz.objects.filter(qname="quiztime").first()
time_for_quiztime_hours=quiz.end.strftime('%H')
time_for_quiztime_minutes=quiz.end.strftime('%M')

wklyquiz=Quiz.objects.filter(qname="weeklyquiz").first()
time_for_wklyquiz_hours=quiz.end.strftime('%H')
time_for_wklyquiz_minutes=quiz.end.strftime('%M')

wkndquiz=Quiz.objects.filter(qname="weekendquiz").first()
time_for_wkndquiz_hours=quiz.end.strftime('%H')
time_for_wkndquiz_minutes=quiz.end.strftime('%M')


@periodic_task(run_every=crontab(hour=int(time_for_quiztime_hours), minute=int(time_for_quiztime_minutes)))
def getwinners():
    winne=random.sample(eligible,2)
    winners.create(username=winne[0].username,isrewarded=False)
    winners.create(username=winne[1].username,isrewarded=False)
    for winn in winne:
        user=User.objects.get(username=winn.username)
        mail_subject = 'Congo!! You are one of the reward winner.'
        message = render_to_string('eligible.html', {
        'user': user,
        })
        to_email =user.email
        email = EmailMessage(
        mail_subject, message, to=[to_email]
        )
        email.send()
    eligible.objects.all().delete()





@periodic_task(run_every=crontab(hour=int(time_for_wklyquiz_hours), minute=int(time_for_wklyquiz_minutes)))
def getwinnerswklyquiz():
    winne=random.sample(eligible,2)
    winners.create(username=winne[0].username,isrewarded=False)
    winners.create(username=winne[1].username,isrewarded=False)
    for winn in winne:
        user=User.objects.get(username=winn.username)
        mail_subject = 'Congo!! You are one of the reward winner.'
        message = render_to_string('eligible.html', {
        'user': user,
        })
        to_email =user.email
        email = EmailMessage(
        mail_subject, message, to=[to_email]
        )
        email.send()
    eligible.objects.all().delete()




@periodic_task(run_every=crontab(hour=int(time_for_wkndquiz_hours), minute=int(time_for_wkndquiz_minutes)))
def getwinnerswkndquiz():
    winne=random.sample(eligible,2)
    winners.create(username=winne[0].username,isrewarded=False)
    winners.create(username=winne[1].username,isrewarded=False)
    for winn in winne:
        user=User.objects.get(username=winn.username)
        up=UserProfile.objects.get(username=winn.username)
        up.wins=up.wins+1
        mail_subject = 'Congo!! You are one of the reward winner.'
        message = render_to_string('eligible.html', {
        'user': user,
        })
        to_email =user.email
        email = EmailMessage(
        mail_subject, message, to=[to_email]
        )
        email.send()

    eligible.objects.all().delete()


@periodic_task(run_every=crontab(hour=int(time_for_quiztime_hours), minute=int(time_for_quiztime_minutes)))
def userspar():
    users=UserProfile.objects.all()
    for user in users:
        user.parquiztime=False
        user.save()



@periodic_task(run_every=crontab(hour=int(time_for_wklyquiz_hours), minute=int(time_for_wklyquiz_minutes)))
def usersparwklyquiz():
    users=UserProfile.objects.all()
    for user in users:
        user.parwklyquiz=False
        user.save()

@periodic_task(run_every=crontab(hour=int(time_for_wklyquiz_hours), minute=int(time_for_wklyquiz_minutes)))
def usersparwkndquiz():
    users=UserProfile.objects.all()
    for user in users:
        user.parwklyquiz=False
        user.save()
