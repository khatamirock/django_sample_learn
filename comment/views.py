
from email.policy import HTTP
from django.shortcuts import render
from rest_framework import viewsets

import comment
from .models import Post, Comment
from rest_framework.decorators import action
from .serializers import PostSerializer, CommentSerializer
from django.http import HttpResponse
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    serializer_class = PostSerializer


def post_detail(request, id):
        # fetch related comment
    comments = Comment.objects.filter(post=id)
    # get  post with
    post = Post.objects.get(id=id)
    print(post)
    str = post.title + '         \n'
    for x in comments:
        str += x.content + '\t\n'
    return render(request, 'post.html', {'post': post, 'comments': comments})

    # return HttpResponse(str)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# python manage.py makemigrations
# python manage.py migrate
