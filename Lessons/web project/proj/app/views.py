from django.shortcuts import render
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
    Post.objects.all()
    return None

def post(request, post_id):
    try:
        p = Post.objects.get(id=post_id)
        context = {}
        context['title'] = p.title
        context['id'] = p.id
        context['content'] = p.content
        return render(request, 'micro_post.html', context)
    except:
        return django.http.HttpResponseNotFound("not found")

def add_post(request):
    pass