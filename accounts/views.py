from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User
from .models import UserProfile
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']    
        password=request.POST['password']       
        confirm_password=request.POST['confirm_password']
        email.lower()
        if username=="":
            messages.info(request,'Enter Username!')
            return redirect('accounts:register')
        if email=="":
            messages.info(request,'Enter Email ID !')
            return redirect('accounts:register')
        if password=="":
            messages.info(request,'Enter a Password!')
            return redirect('accounts:register')
        if confirm_password=="":
            messages.info(request,'Confirm Password!')
            return redirect('accounts:register')
        if " " in username:
            messages.info(request,'Username should not contain spaces')
            return redirect('accounts:register')
        if username[0].isdigit():
            messages.info(request,'First letter of Username should not contain number')
            return redirect('accounts:register')

        
        if not request.POST.get('agree', None) == None:

        
            if password==confirm_password:
                if(len(password)<8):
                    messages.info(request,'Password too weak')
                    return redirect('accounts:register')
                if username==password:
                    messages.info(request,'Password should not be same as username')
                    return redirect('accounts:register')
                if email==password:
                    messages.info(request,'Password should not be same as Email-ID')
                    return redirect('accounts:register')    
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username already registered')
                    return redirect('accounts:register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'email-id already registered')
                    return redirect('accounts:register')
                else:
                    user=User.objects.create_user(username=username,password=password,email=email)
                    
                    mail_subject = 'Activate your GCUVault account.'
                    message = render_to_string('email.html', {
                    'user': user,
                    'domain': get_current_site(request).domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':account_activation_token.make_token(user),
                    })
                    to_email =email
                    email = EmailMessage(
                    mail_subject, message, to=[to_email]
                    )
                   
                    email.send()
                    user.is_active=False
                    user.save()
                    messages.info(request,'Please verify your email to login !')
                    return redirect('accounts:login')

            else:
                messages.info(request,'Passwords are not matching')
                return redirect('accounts:register')
        else:
            messages.info(request,'Please agree to terms and conditions!')
            return redirect('accounts:register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        
        if user is not None and user.is_active==False:
            messages.info(request,'You haven\'t verified your email.Please check your mail')
            return redirect('login')
        elif user is not None:
            auth.login(request,user)
            if not request.POST.get('remember_me', None):
                request.session.set_expiry(0)
            return redirect('vault:home')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('accounts:login')
        

    else:    
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('vault:home')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
            # activate user and login:
        user.is_active = True
        user.save()
        return render(request, 'login.html', {'messages':"Email Verified! You can login Now!"})

    else:
        return render(request, 'login.html', {'messages':"Invalid activation link!"})

def forgotpassword(request):
    if request.method=='POST':
        email=request.POST['email']
        user=User.objects.get(email=email)
        if User.objects.filter(email=email).exists():
            
            mail_subject = 'Activate your blog account.'
            message = render_to_string('fp.html', {
            'user': user,
            'domain': get_current_site(request).domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activation_token.make_token(user),
            })
            to_email =email
            email = EmailMessage(
            mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request,'passwordlinksent.html',{'resetmess':"A Password reset link has been sent to your E-mail ID. Open the link to reset your Password"})
        
        else:
            messages.info(request,'Invalid Email-id')
            return redirect('forgotpassword')
    else:
        return render(request,'forgotpassword.html')

def reset(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        request.session['uid'] = uid
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        
        return redirect('resetpassword')
    else:
        return render(request, 'passwordlinkreset.html',{'messages':"Invalid activation link !"})

def resetpassword(request):
    try:
        id=request.session.get('uid')
        user = User.objects.get(pk=id)
        request.session.pop('token', None) 
        request.session.modified = True
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None:
        print('user is not none')
        if request.method=="POST":
            new_password=request.POST['password']
            confirm_new_password=request.POST['confirm_password']
            if new_password=="":
                messages.info(request,'Enter a Password!')
                return redirect('register')
            if confirm_new_password=="":
                messages.info(request,'Please Confirm Password!')
                return redirect('register')
            if new_password==confirm_new_password:
                if(len(new_password)<8):
                    messages.info(request,'Password too weak')
                    return redirect('register')
                if user.username==new_password:
                    messages.info(request,'Password should not be same as username')
                    return redirect('register')
                if user.email==new_password:
                    messages.info(request,'Password should not be same as Email-ID')
                    return redirect('register')
                user.is_active=True
                user.set_password(new_password) 
                user.save()
                return render(request,'login.html',{'mess':"Password Reset Success"})
        else:    
            return render(request,'resetpassword.html')
    else:
        return render(request,'error404.html')


def editprofile(request):
    if request.method=='POST':
        user=request.user
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        phone=request.POST['mobile']
        gender=request.POST.get('gender')
        propic=request.FILES.get('propic')  
        if first_name=="" or last_name=="":
            messages.info(request,'Enter first name and last name')
            return redirect('accounts:editprofile')
        if phone=="":
            messages.info(request,'Please enter mobile number')
            return redirect('accounts:editprofile')
        if gender==None:
            messages.info(request,'Please select gender')
            return redirect('accounts:editprofile')
        if propic==None:
            propic=user.userprofile.profilepic
        user.first_name=first_name
        user.last_name=last_name
        user.userprofile.phone=phone
        user.userprofile.gender=gender
        user.userprofile.profilepic=propic
        user.save()
        user.userprofile.save()
        return redirect('vault:home')        
    else:
        return render(request,'editprofile.html')


def profile(request):
    user=request.user
    userpro="None"
    if user.is_authenticated:
        userpro=UserProfile.objects.get(user=user)
    return render(request,'profile.html',{'user':user,'userpro':userpro})


def rewards(request):
    return render(request,'rewards.html')

def tandc(request):
    return render(request,'tandc.html')



