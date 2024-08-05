from django.urls import path
from .views import (
    AuthorBlogsListView,
    AllBlogsListView,
    BlogsDetailView,
    BlogsCreateView,
    BlogsUpdateView,
    BlogsDeleteView,
)
urlpatterns=[
    path('all/',AllBlogsListView.as_view(),name='all-blogs-list'),
    path('author/<str:username>/',AuthorBlogsListView.as_view(),name='author-blogs-list'),
    path('author/<str:username>/<int:pk>/',BlogsDetailView.as_view(),name='blogs-detail'),
    path('author/<str:username>/new',BlogsCreateView.as_view(),name='blogs-create'),
    path('author/<str:username>/<int:pk>/edit/',BlogsUpdateView.as_view(),name='blogs-edit'),
    path('author/<str:username>/<int:pk>/delete/',BlogsDeleteView.as_view(),name='blogs-delete'),
]