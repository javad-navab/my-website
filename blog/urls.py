from django.urls import path
from blog.views import *
from blog.feeds import LatestEntriesFeed

app_name='blog'
urlpatterns=[
    path('' , blog ,name='blog'),
    path('<int:pid>' , blog_single ,name='single'),
    path('category/<str:cat_name>' , blog ,name='category'),
    path('author/<str:author_username>' , blog ,name='author'),
    path('tag/<str:tag_name>' , blog ,name='tag'),
    path('rss/feed/', LatestEntriesFeed()),
    path('search/' , blog_search ,name='search')
    ]