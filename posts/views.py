from django.http.response import HttpResponseNotFound
from .models import Post
from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostForm




def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/all_posts.html', { 'all_posts': posts})

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('post_detail', pk=news.pk)
    else:
        form = PostForm()
    return render(request, 'posts/post_edit.html', {'form': form})


def post_detail(request, pk):
    post_detail = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post_detail': post_detail})


def post_edit(request, pk):
    posts =get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POSt, instance=posts)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('post_detail', pk=news.pk)
    else:
        form = PostForm(instance=posts)
    return render(request, 'posts/post_edit.html', {'form': form})


def post_delete(request, pk):
    try:
        news = Post.objects.get(id=pk)
        news.delete()
        return redirect('all_posts')
    except:
        return HttpResponseNotFound("<h2>Такой страницы нет</h2>")