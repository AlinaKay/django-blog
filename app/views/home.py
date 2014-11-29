from django.shortcuts import render
from data.models import *

def post_list(request):
    posts=Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    return render(request,'post_list.html',{'posts':posts})
