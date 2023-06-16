from django.shortcuts import render, redirect
from goods.models import Item

def dashboard(request):
    items = Item.objects.filter(seller=request.user)
    return render(request, 'dashboard/index.html',{'items':items})

