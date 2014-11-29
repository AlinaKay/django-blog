from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from app.forms import *
from data.models import *

def post_detail(request,slug):
    post=get_object_or_404(Post,url=slug)
    return render(request,'post_detail.html',{'post':post})

@login_required
def post_new(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('/post/'+post.url)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

@login_required
def post_edit(request, slug):
    print slug
    post = get_object_or_404(Post, url=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/post/'+post.url)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('/')

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('/')
