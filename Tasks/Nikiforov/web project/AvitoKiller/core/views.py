from django.shortcuts import render, redirect
from goods.models import Category, Item
from .forms import CreateUser
from django.contrib.auth import logout 

def index(request):
    goods = Item.objects.all()
    categories = Category.objects.all()
    return render(request, 'core/index.html',{'goods':goods, 'categories':categories,})

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_account/')
    else:
        form = CreateUser()
    return render(request, 'core/signup.html', {'form':form})

def logout_user(request):
    logout(request)
    return redirect('/')
    