from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.

def user_login(request):
    form= LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd =form.cleaned_data
            user=authenticate(request, username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('Alumni_clubs:user_dashboard')
                else:
                    return HttpResponse('Disabled user')
            else:
                return HttpResponse('Invalid login')
        else:
            form= LoginForm()
    return render(request,'login.html',{'form': form})


