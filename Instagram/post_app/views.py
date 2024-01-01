from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.models import Profile
from .models import Post
from django.contrib.auth.models import User


def home(request):
    context = {
        'pro': Profile.objects .all()
    }

    return render(request, 'post_app/home.html', context)


def about(request):
    return render(request, 'post_app/about.html')


class PostListView(ListView):
    model = Post
    template_name = 'post_app/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context.update({
            'porfiles': Profile.objects.all(),
        })
        return context

    def get_queryset(self):
        return Post.objects.all()


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['content', 'image']
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['content', 'image']
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/profile/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author: return True
        return False


class Profile_PostDetailView(ListView):
    model = Post
    template_name = 'post_app/profile_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user)
