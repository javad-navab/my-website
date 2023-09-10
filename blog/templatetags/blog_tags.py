from django import template
from blog.models import post , comment
from blog.models import category


register = template.Library()

@register.simple_tag(name='totalposts')
def function():
    posts = post.objects.filter(status = True).count()
    return posts


@register.simple_tag(name='posts')
def function():
    posts = post.objects.filter(status = True)
    return posts

@register.filter()
def snippet(value , arg=20):
    return value[:arg]


@register.inclusion_tag('blog/blog-popular-posts.html')
def latestposts():
    posts = post.objects.filter(status = True).order_by('-published_at')[:4]
    return {'posts': posts}

@register.simple_tag(name='comments_count')
def function(pid):
    return comment.objects.filter(post = pid , approved = True).count()

@register.inclusion_tag('blog/blog-category.html')
def postcategories():
    posts = post.objects.filter(status = True)
    categories = category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}