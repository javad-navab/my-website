from django import template
from blog.models import post
from blog.models import category


register = template.Library()
@register.inclusion_tag('website/website-recentpost.html')
def recent():
    recentposts = post.objects.filter(status = True).order_by('-published_at')[:6]
    return {'recentposts' : recentposts }