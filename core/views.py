from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login

# Create your views here.

def home(request):
    return render(request,'core/home.html')



@login_required
def products(request):
    return render(request,'core/products.html')
    

def exit(request):
    logout(request)
    return redirect('home')

def register(request):
    contex={
        'form': CustomUserCreationForm
    }

    if request.method == 'POST':
        user=CustomUserCreationForm(data=request.POST)

        if user.is_valid():
            user.save()

            usuario=authenticate(username=user.cleaned_data['username'],password=user.cleaned_data['password1'])
            login(request,usuario)
            return redirect('home')
        

    return render(request,'registration/register.html',contex)