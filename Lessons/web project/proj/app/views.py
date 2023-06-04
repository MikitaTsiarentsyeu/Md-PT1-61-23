from django.shortcuts import render, HttpResponse, redirect
import django.http
from .models import Post, Author
from .forms import AddPost
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator

import datetime

from django.views import View

# Create your views here.
# def home(request):
#     ctime = datetime.datetime.now()
#     return render(request, "home.html", {"time":ctime})

# def test_view(request, param):
#     param_type = type(param)
#     print(f"{param}:{param_type}")
#     return render(request, "home.html", {"time":param_type})

class PostModelViewBase:

    model = Post
    page_size = 2

    def get_all_posts(self):
        return self.model.objects.all()
    
    def get_page(self, page_number):
        posts = self.get_all_posts()
        paginator = Paginator(posts, self.page_size)
        page_obj = paginator.get_page(page_number)
        return page_obj
    
    def get_post(self, post_id):
        try:
            p = self.model.objects.get(id=post_id)
            return p
        except:
            return False
        
    def add_post(self, form, author):
        if form.is_valid():
            post_entry = form.save(commit=False)
            post_entry.author = author
            post_entry.issued = datetime.datetime.now()
            post_entry.save()
            return post_entry.id

class SessionViewBase:

    session_key = 'viewed'

    def get_post_ids(self, request):
        return request.session.get(self.session_key, [])
    
    def set_post_id(self, request, id):
        viewed = self.get_post_ids(request)
        if id not in viewed:
            viewed.append(id)
            request.session[self.session_key] = viewed


class PostsView(PostModelViewBase, SessionViewBase, View):

    template = 'posts.html'

    def get(self, request):
        viewed = super().get_post_ids(request)
        page_number = request.GET.get('page')
        page_obj = super().get_page(page_number)
        context = {}
        context['viewed'] = viewed
        context['page_obj'] = page_obj
        return render(request, self.template, context)

# def posts(request):
#     posts = Post.objects.all()
#     paginator = Paginator(posts, 2)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     viewed = request.session.get('viewed', [])
#     context = {}
#     # context['posts'] = posts
#     context['viewed'] = viewed
#     context['page_obj'] = page_obj
#     print(viewed)
#     return render(request, 'posts.html', context)

class PostView(PostsView):

    template = 'post.html'

    def get(self, request, post_id):
        print(post_id)
        p = super().get_post(post_id)
        if p:
            super().set_post_id(request, post_id)
            context = {}
            context['post'] = p
            return render(request, 'post.html', context)
        else:
            return django.http.HttpResponseNotFound("not found")

# def post(request, post_id):
#     try:
#         p = Post.objects.get(id=post_id)
#         viewed = request.session.get('viewed', [])
#         if p.id not in viewed:
#             viewed.append(p.id)
#             request.session['viewed'] = viewed
#         context = {}
#         context['post'] = p
#         return render(request, 'post.html', context)
#     except:
#         return django.http.HttpResponseNotFound("not found")

class AddPosView(PostModelViewBase, View):

    template = 'add_post.html'
    
    def get(self, request):
        form = AddPost()
        return render(request, self.template, {'form':form})

    def post(self, request):
        form = AddPost(request.POST, request.FILES)

        if form.is_valid():
            id = super().add_post(form, Author.objects.get(email=request.user.email))

            return redirect('post', id)


# @permission_required("app.add_post")
# def add_post(request):
#     if request.method == "POST":
#         form = AddPost(request.POST, request.FILES)

#         if form.is_valid():
#             # post_entry = Post()
#             # post_entry.title = form.cleaned_data['title']
#             # post_entry.content = form.cleaned_data['content']
#             # post_entry.image = form.cleaned_data['image']
#             # post_entry.post_type = form.cleaned_data['post_type']
#             # post_entry.author = Author.objects.all()[0]
#             # post_entry.issued = datetime.datetime.now()
#             # post_entry.save()


#             post_entry = form.save(commit=False)
#             post_entry.author = Author.objects.get(email=request.user.email)
#             post_entry.issued = datetime.datetime.now()
#             post_entry.save()
#             # form.save_m2m()

#             return redirect('post', post_entry.id)

#     else:
#         form = AddPost()

#     return render(request, 'add_post.html', {'form':form})