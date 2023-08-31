from django.shortcuts import render , get_object_or_404
from blog.models import post
from website.models import contact
import datetime
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger

# Create your views here.
def blog(request , **kwargs):
    t = datetime.datetime.now()
    posts = post.objects.filter( status=True , published_at__lte=t)
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username'):
        posts = posts.filter(author__username=kwargs['author_username'])
    posts = Paginator(posts ,6)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts' : posts }
    return render(request,'blog/blog-home.html' , context)

def blog_single(request , pid):
    t = datetime.datetime.now()
    posts = post.objects.get(id=pid)
    posts.counted_views=posts.counted_views+1
    posts.save()
    posts = get_object_or_404(post,id=pid , status = True)
    next = post.objects.filter(id__gt=pid , status = True).order_by('id').first()
    pre = post.objects.filter(id__lt=pid  , status = True).order_by('-id').first()
    context = {'post':posts , 'next':next , 'pre':pre}
    return render(request,'blog/blog-single.html' , context)


def blog_category(request,cat_name):
    posts = post.objects.filter(status=True)
    posts = posts.filter(category__name=cat_name)
    context = {'posts': posts }
    return render(request,'blog/blog-home.html' , context)

def blog_search(request,):
    posts = post.objects.filter(status=True)
    if request.method == 'GET':
        if s:=request.GET.get('search'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html' , context)
