from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import post

class LatestEntriesFeed(Feed):
    title = "bliog newest post"
    link = "/rss/feed"
    description = "one of the first blogs that i have ever created"

    def items(self):
        return post.objects.filter(status=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content
