from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog_Vlog_Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .forms import CustomUserCreationForm
from django.contrib import messages

# Create your views here.

menu = [
        {'title': 'Add Post', 'url_name': 'add_post'},
        {'title': 'Edit/Delete', 'url_name': 'edit_delete'},
        {'title': 'Register', 'url_name': 'register'},
        {'title': 'Login', 'url_name': 'login'}
]

def home(request):
    posts = Blog_Vlog_Post.objects.all().order_by('-created_on')
    data = {'menu': menu, 'posts': posts, 'title': 'Home Page'}
    return render(request, 'app_blog_vlog/home.html', context = data)

def show_post(request, post_id):
    post = get_object_or_404(Blog_Vlog_Post, pk = post_id)
    return render(request, 'app_blog_vlog/show_post.html', {'post': post})



@login_required(login_url='/login/')
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'app_blog_vlog/add_post.html', {'form': form, 'title': 'Add Post Page'})



@login_required(login_url='/login/')
def edit_delete(request):
    user_posts = Blog_Vlog_Post.objects.filter(author=request.user)
    data3 = {'title': 'Edit/Delete Post', 'user_posts': user_posts}
    return render(request, 'app_blog_vlog/edit_delete.html', data3)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'app_blog_vlog/register.html', {'form': form, 'title': 'Register Page'})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'app_blog_vlog/login.html', {'form': form, 'title': 'Login Page'})


def edit_post(request, post_id):
    post = get_object_or_404(Blog_Vlog_Post, pk=post_id, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('edit_delete')
    else:
        form = PostForm(instance=post)
    return render(request, 'app_blog_vlog/edit_post.html', {'form': form, 'post': post})


def delete_post(request, post_id):
    post = get_object_or_404(Blog_Vlog_Post, pk=post_id, author=request.user)
    post.delete()
    return redirect('edit_delete')


from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):
    logout(request)
    return redirect('home')


from .models import Comment

# Add this function to handle comment submission
@login_required(login_url='/login/')
def add_comment(request, post_id):
    post = get_object_or_404(Blog_Vlog_Post, pk=post_id)
    
    if request.method == 'POST':
        text = request.POST.get('comment_text')
        Comment.objects.create(post=post, author=request.user, text=text)
        return redirect('show_post', post_id=post_id)
    
    return render(request, 'app_blog_vlog/show_post.html', {'post': post})



