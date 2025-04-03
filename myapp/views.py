
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from .forms import LoginForm, SignUpForm
from .models import Profile
import random 
import http.client
from django.conf import settings
from .helper import MessageHandler
# Create your views here.
from django.contrib.auth.decorators import login_required

from django.contrib.auth.backends import BaseBackend
from .models import Profile
from django.contrib.auth.models import User

class OTPBackend(BaseBackend):
    def authenticate(self, request, mobile=None, otp=None):
        try:
            profile = Profile.objects.get(mobile=mobile, otp=otp)
            return profile.user
        except Profile.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

#login page
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, HttpResponse
import random
from .forms import LoginForm, OTPLoginForm
from .models import Profile

def send_otp(mobile):
    otp = random.randint(1000, 9999)
    try:
        profile = Profile.objects.get(mobile=mobile)
        profile.otp = otp
        profile.save()
        # Replace with actual sending logic
        messagehandler = MessageHandler(mobile, otp)
        messagehandler.send_otp_via_message()
    except Profile.DoesNotExist:
        return None  # Return None if the profile does not exist
    return otp

def authlogin(request):
    msg = ""
    if request.method == 'POST':
        if 'username' in request.POST:
            login_form = LoginForm(request.POST)
            otp_form = OTPLoginForm()
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect('home')
                else:
                    msg = 'Invalid credentials'
            else:
                msg = 'Error validating the login form. Please try again!'
        else:
            login_form = LoginForm()
            otp_form = OTPLoginForm(request.POST)
            if otp_form.is_valid():
                mobile = otp_form.cleaned_data['mobile']
                otp = otp_form.cleaned_data['otp']
                if otp:
                    user = authenticate(request, mobile=mobile, otp=otp)
                    if user:
                        user.backend = 'yourapp.backends.OTPBackend'
                        login(request, user)
                        return redirect('home')
                    else:
                        msg = "Invalid OTP"
                else:
                    otp = send_otp(mobile)
                    if otp:
                        request.session['otp_sent'] = True
                        request.session['otp'] = otp
                        request.session['mobile'] = mobile
                        return redirect('otp_verify')
                    else:
                        msg = "Mobile number not registered"
            else:
                msg = "Error validating the OTP form. Please try again!"
    else:
        login_form = LoginForm()
        otp_form = OTPLoginForm()

    return render(request, 'authlogin.html', {'form': login_form, 'otp_form': otp_form, 'msg': msg})

def otp_verify(request):
    mobile = request.session.get('mobile')
    otp = request.session.get('otp')
    msg = ""

    if request.method == 'POST':
        otp_form = OTPLoginForm(request.POST)

        if otp_form.is_valid():
            entered_otp = otp_form.cleaned_data['otp']

            if entered_otp == str(otp):
                try:
                    profile = Profile.objects.get(mobile=mobile)
                    user = profile.user
                    user.backend = 'myapp.backends.OTPBackend'
                    login(request, user, backend='myapp.backends.OTPBackend')

                    request.session.pop('otp_sent', None)
                    return redirect('home')
                except Profile.DoesNotExist:
                    msg = "Profile does not exist"
            else:
                msg = "Invalid OTP"
        else:
            msg = "Error validating the form. Please try again!"

    else:
        otp_form = OTPLoginForm()

    return render(request, 'otp_verify.html', {'form': otp_form, 'mobile': mobile, 'msg': msg})

# Regisgration Page 
def authregister(request):
    
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            mobile=form.cleaned_data.get("mobile")
            
            check_user=Profile.objects.filter(mobile=mobile).first()
            if check_user:
                context={'message':'Mobile Number is already Registred,Go To Login Page'}
                return render(request,'authregister.html',context)
            
            profile = authenticate(mobile=mobile)
            user = authenticate(username=username, password=raw_password)
            user.save()
            
            #otp generator
            otp=random.randint(1000,9999)
            profile = Profile(user = user , mobile=mobile,otp=otp) 
            profile.save()
            messagehandler=MessageHandler(mobile,otp).send_otp_via_message() 
            request.session['mobile'] = mobile
            return redirect('otp/')
        
            #msg = 'Your Account has been successfully created!! <a href="/login">login</a>.'
            # success = True
            #return redirect("/authlogin/")

        else:
            msg = 'Check Your Entered Data Carefully '
    else:
        form = SignUpForm()

    return render(request, "authregister.html", {"form": form, "msg": msg, "success": success})
def otpVerify(request):
    mobile = request.session['mobile']
    context = {'mobile':mobile}
    
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = Profile.objects.filter(mobile=mobile).first()
        
        if otp == profile.otp:
            return redirect('home')
        else:
            print('Wrong')
            
            context = {'message' : 'Wrong OTP' , 'class' : 'danger','mobile':mobile }
            return render(request,'otp.html' , context)
            
        
    return render(request,'otp.html' , context)



#Logout
def LogoutPage(request):
    logout(request)
    return redirect('authlogin')
#Landing Page

def mainpage(request):
    return render(request,'main.html')
#About Page 
def about(request):
    return render(request,'about.html')
#Contact Page
def contact(request):
    return render(request,'contact.html')
#otp page 
def otp(request):
    return render(request,'otp.html')
#Home Page
@login_required(login_url='/authlogin/')
def HomePage(request):
     user = request.user #the user
     email = user.email #their email
     username = user.username #their username
     return render(request,'main.html')
#indexpage
@login_required(login_url='/authlogin/')
def IndexPage(request):
    return render(request,'index.html')
#base page
def basePage(request):
    return render(request,'base.html')
def soil_track(request):
    return render(request,'track_soil_test.html')
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CustomPasswordChangeForm

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def view_profile(request):

    return render(request, 'view_profile.html', {'user': request.user})


from .forms import EditProfileForm
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('view_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})


# weather
import requests


def weather_view(request):
    api_key = '4f80a23f86c76378175438fff6a163e6'  # Replace with your OpenWeatherMap API key
    weather_data = None
    if 'city' in request.GET:
        city = request.GET['city']
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=4f80a23f86c76378175438fff6a163e6&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            weather_data['icon'] = get_weather_icon(weather_data['weather'][0]['main'])
    return render(request, 'weather.html', {'weather_data': weather_data})

def get_weather_icon(weather_description):
    icons = {
        'Clear': 'fas fa-sun',
        'Clouds': 'fas fa-cloud',
        'Rain': 'fas fa-cloud-showers-heavy',
        'Drizzle': 'fas fa-cloud-rain',
        'Thunderstorm': 'fas fa-bolt',
        'Snow': 'fas fa-snowflake',
        'Mist': 'fas fa-smog',
        'Fog': 'fas fa-smog',
    }
    return icons.get(weather_description, 'fas fa-question')
