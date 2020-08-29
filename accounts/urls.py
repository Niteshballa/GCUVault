from django.contrib import admin
from django.urls import path
from . import views

app_name="accounts"
urlpatterns=[
    
     path('login',views.login,name='login'),
     path('register',views.register,name='register'),
     path('logout',views.logout,name='logout'),
     path('editprofile',views.editprofile,name="editprofile"),
     path('profile',views.profile,name="profile"),
     path('termsandconditions',views.tandc,name="termsandconditions"),
     path('forgotpassword',views.forgotpassword,name="fp"),
     path('reset/<str:uidb64>/<str:token>',views.reset,name="reset"),
     path('resetpassword',views.resetpassword,name="resetpassword"),
     path('activate/<str:uidb64>/<str:token>', views.activate, name='activate'),
]