from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Post
from .forms import PostForm, UserRegisterForm
from django.contrib import messages

# Create your views here.
def home(request):
    """Display all blog posts"""
    if request.user.is_authenticated:
        if request.user.is_superuser:
            posts = Post.objects.all().order_by('-created_at')
        else:
            posts = Post.objects.all().order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blogapp/home.html', {'posts': posts})


def signup(request):
    """Handle user registration"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserRegisterForm()
    
    return render(request, 'blogapp/signup.html', {'form': form})


@login_required(login_url='login')
def create_post(request):
    """Handle blog post creation"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post published successfully!')
            return redirect('post_detail', post_id=post.id)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = PostForm()
    
    return render(request, 'blogapp/create_post.html', {'form': form})


def post_detail(request, post_id):
    """Display individual blog post"""
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blogapp/post_detail.html', {'post': post})