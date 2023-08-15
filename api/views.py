from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Blog
from .BlogSerializer import BlogSerializer
from rest_framework.response import Response


# Create your views here.


@api_view(['GET'])
def Blogs(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

