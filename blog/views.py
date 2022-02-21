from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404,
)
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
                            # messages.debug
                            # messages.info
                            # messages.success
                            # messages.warning
                            # messages.error

from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Post
from .forms import (
    UserRegisterForm, 
    UserUpdateForm, 
    ProfileUpdateForm,
)

# Create your views here.

posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context = {
        # 'posts': posts,
        'posts' : Post.objects.all(),
        'title': "Home"
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username} ! ')
            # return redirect('blog:blog-home') # redirect to the homepage after registration
            return redirect('blog:blog-login') # redirect to the login page after registration
    else :
        form = UserRegisterForm()

    content = {
        'form': form,
    }
    return render(request, 'blog/register.html', content)

@login_required
def profile(request):
    if request.method == 'POST' :
        userUpdateForm = UserUpdateForm(request.POST, instance=request.user)
        profileUpdateForm = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if userUpdateForm.is_valid() and profileUpdateForm.is_valid():
            userUpdateForm.save()
            profileUpdateForm.save()

            messages.success(request, f'Your profile has been updated! ')
            return redirect('blog:blog-profile') # redirect to the login page after registration

    else :
        userUpdateForm = UserUpdateForm(instance=request.user)
        profileUpdateForm = ProfileUpdateForm(instance=request.user.profile)
    context = {
        "userUpdateForm" : userUpdateForm,
        "profileUpdateForm" : profileUpdateForm,
    }
    return render(request, 'blog/profile.html', context)


class PostListView(ListView):
    """
    Those variables are pre-defined (use it as like) :
        template_name
        context_object_name
    """
    model = Post
    template_name = 'blog/home.html' # <app_name>/<view_page>.html
    context_object_name = 'posts'
    ordering = [
        # '-datePosted',
        'datePosted',
    ]
    paginate_by = 3


class UserPostListView(ListView):
    """
    Those variables are pre-defined (use it as like) :
        template_name
        context_object_name
    """
    model = Post
    template_name = 'blog/user_posts.html' # <app_name>/<view_page>.html
    context_object_name = 'posts'

    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('datePosted')
    
class PostDetailView(DetailView):
    model = Post
    # do not you need to this line ??????????????
    # template_name = 'blog/post_detail.html' # <app_name>/<view_page>.html


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # template_name = 'blog/post_form.html' # <app_name>/<view_page>.html
    fields = [
        'title',
        'content',
    ]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    # template_name = 'blog/post_form.html' # <app_name>/<view_page>.html
    fields = [
        'title',
        'content',
    ]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # do not you need to this line ??????????????
    # template_name = 'blog/post_detail.html' # <app_name>/<view_page>.html

    success_url = '/blog '
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False