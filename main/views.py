from django.shortcuts import render,redirect
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.
def homepage(request):
    post={'Tuts':Tutorial.objects.all}
    return render(request,'main/home.html',context=post)

def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'New account created: {username}')
            login(request,user)
            return redirect('main:home_page')
        else:
            for msg in form.error_messages:
                messages.error(request,f'{msg}:{form.error_messages[msg]}')

    form=UserCreationForm
    return render(request,'main/register.html',context={'form':form})
