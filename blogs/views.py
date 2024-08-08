from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import blogs
# Create your views here.

class AllBlogsListView(ListView):
    model=blogs
    template_name='pages/all_blogs_list.html'
    context_object_name='blogs'

    def get_queryset(self):
        return blogs.objects.all()

class AuthorBlogsListView(ListView):
    model=blogs
    template_name='pages/author_blogs_list.html'
    context_object_name='blogs'

    def get_queryset(self):
        return blogs.objects.filter(author=self.request.user)

class BlogsDetailView(DetailView):
    model=blogs
    template_name='pages/blogs_detail.html'

class BlogsCreateView(CreateView):
    model=blogs
    template_name='pages/blogs_create.html'
    fields=['title','body','author']

class BlogsUpdateView(UpdateView):
    model=blogs
    template_name='pages/blogs_update.html'
    fields=['title','body']

class BlogsDeleteView(DeleteView):
    model=blogs
    template_name='pages/blogs_delete.html'

    def get_success_url(self):
        return reverse_lazy('author-blogs-list',args=[self.object.author])
