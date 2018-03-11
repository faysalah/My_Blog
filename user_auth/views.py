from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
# Create your views here.
# @login_required(login_url='/accounts/login/')
# @user_passes_test(lambda u:u.is_superuser, login_url='/accounts/login/')
def index(request):
    return redirect('/article')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form .cleaned_data['password1']
            user = authenticate(username=username, password=password)
            print(user)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
        context = { 'form' : form }
        return render(request, 'registration/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('/accounts/login')