from django.shortcuts import render
from .models import MyPost
from django.utils import timezone


def index(request):
    posts = MyPost.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)
