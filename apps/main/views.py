from django.shortcuts import render, redirect
from auths.mixins import LoginMixin
from django.views import View
from .forms import PostForm, CommentForm
from .models import Post
from django.core.paginator import Paginator

class CreatePostView(LoginMixin, View):
    def get(self, request):
        form = PostForm()
        return render(request, 'main/create_post.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
        return render(request, 'main/create_post.html', {'form': form})

class HomeView(View):
    def get(self, request):
        post_list = Post.objects.all()
        paginator = Paginator(post_list, 5)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        comment_form = CommentForm()
        return render(request, 'main/home.html', {'posts': posts, 'comment_form': comment_form})

    def post(self, request):
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post_id = request.POST.get('post_id')
            comment.save()
            return redirect('home')
        posts = Post.objects.all()
        return render(request, 'main/home.html', {'posts': posts, 'comment_form': comment_form})
    
class CreateAudioPostView(LoginMixin, View):
    def get(self, request):
        form = PostForm()
        return render(request, 'main/create_audio.html', {'form': form})
    
    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')  
        return render(request, 'main/create_audio.html', {'form': form})

