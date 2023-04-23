
from email.policy import HTTP
from urllib import request
from django.shortcuts import render
from rest_framework import viewsets
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
    str = post.title + '         \n'
    for x in comments:
        str += x.content + '\t\n'
    return render(request, 'post.html', {'post': post, 'comments': comments})

    # return HttpResponse(str)


def postView(request):
    posts = Post.objects.all()

    return render(request, 'main_timeline.html', {'posts': posts})


def addPost(request):
    print('via rei vaii')
    return render(request, 'postSaver.html')


def submit_form(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        print(title, content)
        post=Post(title=title, content=content)
        post.save()
        return postView(request)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
