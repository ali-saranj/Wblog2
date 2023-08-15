from django.contrib import admin
from django.urls import path,include
from .views import Blogs

urlpatterns = [
    path('showBlog/',Blogs),

]