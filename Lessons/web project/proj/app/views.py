from django.shortcuts import render, HttpResponse, redirect
import django.http
from .models import Post, Author
from .forms import AddPost

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
    if request.method == "POST":
        form = AddPost(request.POST, request.FILES)

        if form.is_valid():
            # post_entry = Post()
            # post_entry.title = form.cleaned_data['title']
            # post_entry.content = form.cleaned_data['content']
            # post_entry.image = form.cleaned_data['image']
            # post_entry.post_type = form.cleaned_data['post_type']
            # post_entry.author = Author.objects.all()[0]
            # post_entry.issued = datetime.datetime.now()
            # post_entry.save()


            post_entry = form.save(commit=False)
            post_entry.author = Author.objects.get(email=request.user.email)
            post_entry.issued = datetime.datetime.now()
            post_entry.save()
            # form.save_m2m()

            return redirect('post', post_entry.id)

    else:
        form = AddPost()

    return render(request, 'add_post.html', {'form':form})