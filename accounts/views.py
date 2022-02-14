from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login



def indexView(request):
    return render(request, 'index.html')

@login_required
def dashboardView(request):
    return render(request, 'dashboard.html')

def registerView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        tag = request.POST.get('tag')
        Register=authenticate(request, username=username, password=password, tag=tag)
        if form.clean():
            return redirect('login_url')
    
    else :
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

