from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http import JsonResponse
from .forms import PostForm,CommentForm
from .models import Post


# Create your views here.

# all list blogs
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

# post new blog
def create_blog(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog_create.html', {'form': form })


# get detail page of blog
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.all()
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            try:
                comment = form.save(commit=False)
                comment.post = post
                comment.name = request.user.username
                comment.active = True
                comment.save()

                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({
                        'name': comment.name,
                        'body': comment.body,
                        'created': comment.created
                    })
                else:
                    return redirect('post_detail', id=post.id)
            except Exception as e:
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'error': str(e)}, status=400)
                else:
                    raise e

    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    return render(request, 'post_detail.html', context)





# update post
def update_post(request, id):
    blog = Post.objects.get(id = id)
    print(blog)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm(instance=blog)
    return render(request, 'update_post.html', {'form': form})
    

def delete_post(request, id):
    blog = Post.objects.get(id = id)
    if request.method == 'POST':
        blog.delete()
        return redirect('home')
    return render(request, 'delete_post.html')


# =============AUTHENTICATION=================

def loginUser(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password').lower()
        print('username', username)
        print('password', password)
        try:
            user = User.objects.get(username = username)
            user = authenticate(request, username=username,password=password)
            
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                message = "credentials Invalid"
        except:
                message = "User does not exists"
    context = {'message': message}
    return render(request,'login.html', context)

# Logout Function
def user_logout(request):
    logout(request)
    return redirect('home')


# signUp function
def signUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return redirect(reverse_lazy('login'))
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'signup.html', context)


# def CommentView(request, id):
#     post = Post.objects.get(id=id)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.name = request.user.username 
#             comment.active = True  # Set the active field
#             comment.save()
#             return redirect('home')
#     else:
#         form = CommentForm()

#     context = {'form': form}
#     return render(request, 'post_comment.html', context)


# def get_all_comments(request):
#     comments = Comment.objects.all()
#     return 
    