from django.shortcuts import render, HttpResponse
import django.http
from .models import Post

import datetime

# Create your views here.
def home(request):
    ctime = datetime.datetime.now()
    return render(request, "home.html", {"time":ctime})

def test_view(request, param):
    param_type = type(param)
    print(f"{param}:{param_type}")
    return render(request, "home.html", {"time":param_type})

def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts':posts})

def post(request, post_id):
    try:
        p = Post.objects.get(id=post_id)
        context = {}
        context['post'] = p
        return render(request, 'post.html', context)
    except:
        return django.http.HttpResponseNotFound("not found")

def add_post(request):
    pass