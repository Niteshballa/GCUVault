from django.shortcuts import render,redirect
from .models import Quiz,answer,eligible,winners,contests
from accounts.models import UserProfile
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.utils import timezone
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
# Create your views here.
conts=contests.objects.all()
winnes=winners.objects.all()
def isprofilecomplete(user):
    if user.first_name=="":
        return 0
    if user.last_name=="":
        return 0
    if user.userprofile.phone=="NULL":
        return 0
    if user.userprofile.gender=="NULL":
        return 0
    return 1
    
def quiztime(request):
    user=request.user
    if user.is_authenticated:        
        UserProfile.objects.get_or_create(user=request.user)
        ques=Quiz.objects.get(qname="quiztime")
        if isprofilecomplete(user):
            if  ques.start<=timezone.now() and ques.end>=timezone.now():
                if user.userprofile.parquiztime==False:
                    if request.method=='POST':
                
                        q1ans=request.POST.get('q1')
                        q2ans=request.POST.get('q2')
                        q3ans=request.POST.get('q3')
                        q4ans=request.POST.get('q4')
                        q5ans=request.POST.get('q5')
                        q6ans=request.POST.get('q6')
                        q7ans=request.POST.get('q7')
                        q8ans=request.POST.get('q8')
                        q9ans=request.POST.get('q9')
                        q10ans=request.POST.get('q10')
                        if q1ans==None or q2ans==None or q3ans==None or q4ans==None or q5ans==None or q6ans==None or q7ans==None or q8ans==None or q9ans==None or q10ans==None :
                            messages.info(request,'Please answer all the questions')
                            return redirect('quiz:quiztime')
                        ans=[q1ans,q2ans,q3ans,q4ans,q5ans,q6ans,q7ans,q8ans,q9ans,q10ans]
                        marks=cal(ans,ques.qname)
                        user.userprofile.quiztime=marks
                        user.userprofile.parquiztime=True
                        user.userprofile.quiz=user.userprofile.quiz+1
                        user.userprofile.save()
                        if marks>=9:
                            message='Your score is great. You have chance of winning rewards. Stay Tuned!.You will recieve a mail.  Your Score :'
                            mail_subject = 'Hurray!! You are eligible.'
                            message = render_to_string('eligible.html', {
                            'user': user,
                            })
                            to_email =user.email
                            email = EmailMessage(
                            mail_subject, message, to=[to_email]
                            )
                            email.send()
                            eligible.objects.create(username=user.username)
                        else:
                            message='Better Luck Next time ! Your score : '
                        return render(request,'quizend.html',{'marks':marks,'message':message})
                    elif ques=="":
                        return redirect('quiz:quizover')
                    else:
                        return render(request,'quiztime.html',{'quiz':ques})
                else:
                    return redirect('quiz:quizparticipated')
            else:
                return redirect('quiz:quizover')
        else:
            messages.info(request,'Please complete your profile to play the quiz and win rewards.This information is only used to reach you while sending your rewards to you.')
            return redirect('accounts:editprofile')
    else: 
        return redirect('accounts:login')

    
def weeklyquiz(request):
    user=request.user
    if user.is_authenticated:        
        UserProfile.objects.get_or_create(user=request.user)
        ques=Quiz.objects.get(qname="weeklyquiz")
        if isprofilecomplete(user):
            if  ques.start<=timezone.now() and ques.end>=timezone.now():
                if user.userprofile.parwklyquiz==False:
                    if request.method=='POST':
                
                        q1ans=request.POST.get('q1')
                        q2ans=request.POST.get('q2')
                        q3ans=request.POST.get('q3')
                        q4ans=request.POST.get('q4')
                        q5ans=request.POST.get('q5')
                        q6ans=request.POST.get('q6')
                        q7ans=request.POST.get('q7')
                        q8ans=request.POST.get('q8')
                        q9ans=request.POST.get('q9')
                        q10ans=request.POST.get('q10')
                        if q1ans==None or q2ans==None or q3ans==None or q4ans==None or q5ans==None or q6ans==None or q7ans==None or q8ans==None or q9ans==None or q10ans==None :
                            messages.info(request,'Please answer all the questions')
                            return redirect('quiz:quiztime')
                        ans=[q1ans,q2ans,q3ans,q4ans,q5ans,q6ans,q7ans,q8ans,q9ans,q10ans]
                        marks=cal(ans,ques.qname)
                        user.userprofile.weeklyquiz=marks
                        user.userprofile.parwklyquiz=True
                        user.userprofile.quiz=user.userprofile.quiz+1
                        user.userprofile.save()
                        if marks>=9:
                            message='Your score is great. You have chance of winning rewards. Stay Tuned!.You will recieve a mail.  Your Score :'
                            mail_subject = 'Hurray!! You are eligible.'
                            message = render_to_string('eligible.html', {
                            'user': user,
                            })
                            to_email =user.email
                            email = EmailMessage(
                            mail_subject, message, to=[to_email]
                            )
                            email.send()
                            eligible.objects.create(username=user.username)
                        else:
                            message='Better Luck Next time ! Your score : '
                        return render(request,'quizend.html',{'marks':marks,'message':message})
                    elif ques=="":
                        return redirect('quiz:quizover')
                    else:
                        return render(request,'quiztime.html',{'quiz':ques})
                else:
                    return redirect('quiz:quizparticipated')
            else:
                return redirect('quiz:quizover')
        else:
            messages.info(request,'Please complete your profile to play the quiz and win rewards.This information is only used to reach you while sending your rewards to you.')
            return redirect('accounts:editprofile')
    else: 
        return redirect('accounts:login')

    
def weekendquiz(request):
    user=request.user
    if user.is_authenticated:        
        UserProfile.objects.get_or_create(user=request.user)
        ques=Quiz.objects.get(qname="quiztime")
        if isprofilecomplete(user):
            if  ques.start<=timezone.now() and ques.end>=timezone.now():
                if user.userprofile.parwkndquiz==False:
                    if request.method=='POST':
                
                        q1ans=request.POST.get('q1')
                        q2ans=request.POST.get('q2')
                        q3ans=request.POST.get('q3')
                        q4ans=request.POST.get('q4')
                        q5ans=request.POST.get('q5')
                        q6ans=request.POST.get('q6')
                        q7ans=request.POST.get('q7')
                        q8ans=request.POST.get('q8')
                        q9ans=request.POST.get('q9')
                        q10ans=request.POST.get('q10')
                        if q1ans==None or q2ans==None or q3ans==None or q4ans==None or q5ans==None or q6ans==None or q7ans==None or q8ans==None or q9ans==None or q10ans==None :
                            messages.info(request,'Please answer all the questions')
                            return redirect('quiz:quiztime')
                        ans=[q1ans,q2ans,q3ans,q4ans,q5ans,q6ans,q7ans,q8ans,q9ans,q10ans]
                        marks=cal(ans,ques.qname)
                        user.userprofile.weekeendquiz=marks
                        user.userprofile.parwkndquiz=True
                        user.userprofile.quiz=user.userprofile.quiz+1
                        user.userprofile.save()
                        if marks>=9:
                            message='Your score is great. You have chance of winning rewards. Stay Tuned!.You will recieve a mail.  Your Score :'
                            mail_subject = 'Hurray!! You are eligible.'
                            message = render_to_string('eligible.html', {
                            'user': user,
                            })
                            to_email =user.email
                            email = EmailMessage(
                            mail_subject, message, to=[to_email]
                            )
                            email.send()
                            eligible.objects.create(username=user.username)
                        else:
                            message='Better Luck Next time ! Your score : '
                        return render(request,'quizend.html',{'marks':marks,'message':message})
                    elif ques=="":
                        return redirect('quiz:quizover')
                    else:
                        return render(request,'quiztime.html',{'quiz':ques})
                else:
                    return redirect('quiz:quizparticipated')
            else:
                return redirect('quiz:quizover')
        else:
            messages.info(request,'Please complete your profile to play the quiz and win rewards.This information is only used to reach you while sending your rewards to you.')
            return redirect('accounts:editprofile')
    else: 
        return redirect('accounts:login')

def cal(ans,qname):
    a=answer.objects.get(qname=qname)
    count=0
    if(a.q1ans==ans[0]):
        count=count+1
    if(a.q2ans==ans[1]):
        count=count+1
    if(a.q3ans==ans[2]):
        count=count+1
    if(a.q4ans==ans[3]):
        count=count+1
    if(a.q5ans==ans[4]):
        count=count+1
    if(a.q6ans==ans[5]):
        count=count+1
    if(a.q7ans==ans[6]):
        count=count+1
    if(a.q8ans==ans[7]):
        count=count+1
    if(a.q9ans==ans[8]):
        count=count+1
    if(a.q10ans==ans[9]):
        count=count+1
    return count

def quizend(request):
    return render(request,'quizend.html')


def winner(request):
    if len(winnes)==0:
        return render(request,'nowinner.html')
    else:
        return render(request,'winners.html',{'winners':winnes})

def contest(request):
    if len(conts)==0:
        return render(request,'nocontests.html')
    else:
        return render(request,'contests.html',{'contests':conts})

def quizparticipated(request):
    return render(request,'participated.html')

def quizover(request):
    return render(request,'quizover.html')