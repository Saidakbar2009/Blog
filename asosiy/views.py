from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from .forms import MaqolaForm
# Create your views here.
def maqolalar(request):
    if request.method == 'POST':
        form = MaqolaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/maqolalar/')

    data = {
        'maqolalar': Maqola.objects.all(),
        'form': MaqolaForm()
    }
    return render(request, 'maqolalar.html', data)

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username = request.POST.get('username'),
            password = request.POST.get('password')
        )
        if user:
            login(request, user)
            return redirect('/maqolalar/')
    return render(request, 'register.html')

def sign(request):
    if request.method == 'POST' and request.POST.get('password') == request.POST.get('password2'):
        User.objects.create_user(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        return redirect('/')
    return render(request, 'sign.html')

def log_out(request):
    logout(request)
    return redirect('/')

def malumot(request, id):
    data = {
        'i': Maqola.objects.get(id=id)
    }
    return render(request, 'malumot.html', data)