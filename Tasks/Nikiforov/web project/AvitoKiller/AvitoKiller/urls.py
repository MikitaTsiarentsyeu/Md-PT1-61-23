"""
URL configuration for AvitoKiller project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import index, contact, signup, logout_user
from core.forms import Auth
from goods.views import item_page, new_item, delete_item, edit_item
from dashboard.views import dashboard
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('items/<int:id>', item_page, name='item_page'),
    path('items/<int:id>/delete/', delete_item, name='delete_item'),
    path('items/<int:id>/edit/', edit_item, name='edit_item'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='core/login.html', authentication_form=Auth), name='login'),
    path('logout/', logout_user, name='logout'),
    path('new/', new_item, name='new_item'),
    path('dashboard/', dashboard, name='dashboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
