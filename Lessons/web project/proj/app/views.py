from django.shortcuts import render

import datetime

# Create your views here.
def home(request):
    ctime = datetime.datetime.now()
    return render(request, "home.html", {"time":ctime})