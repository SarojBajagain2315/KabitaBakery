from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from . forms import Loginform
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def register_user(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'new account created')
            return redirect('/register')
        else:
            messages.add_message(request,messages.ERROR,'failed to create an account')
            return render(request,'accounts/register.html',{'forms':form})
    context={
        'forms':UserCreationForm
    }

    return render(request,'accounts/register.html',context)


def postlogin(request):
    if request.method=='POST':
        forms=Loginform(request.POST)
        if forms.is_valid():
            data=forms.cleaned_data
            user=authenticate(request,username=data['username'],password=data['password'])
            if user is not None:
                login(request,user)
                if user.is_staff:
                    return redirect('/admins/dashboard')
                else:
                    return redirect('/')
                return redirect('/products')
            else:
                messages.add_message(request,messages.ERROR,'invalid credintals')
                return render(request,'accounts/login.html',{'forms':forms})

    context={
        'forms':Loginform
    }
    return render(request,'accounts/login.html',context)

def logout_user(request):
    logout(request)
    return redirect('/login')