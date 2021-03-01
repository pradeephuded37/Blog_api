from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from .forms import PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else :
        form = UserRegistrationForm()
    return render(request,'register.html',{'form':form})

@login_required
def profile(request):
    form = PostForm(request.POST)
    if form.is_valid():
        form.save()
        form = PostForm()
    return render(request,'profile.html',{'form':form})