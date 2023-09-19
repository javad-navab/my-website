from django.shortcuts import render , get_object_or_404 , redirect
from blog.models import post , comment
from website.models import contact
import datetime
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from blog.forms import commentForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def blog(request , **kwargs):
    t = datetime.datetime.now()
    posts = post.objects.filter( status=True , published_at__lte=t)
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username'):
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name'):
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
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
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS , 'Comment posted successfully')
        else:
            messages.add_message(request,messages.ERROR , 'Comment not posted successfully')
    t = datetime.datetime.now()
    posts = post.objects.get(id=pid)
    posts.counted_views=posts.counted_views+1
    posts.save()
    posts = get_object_or_404(post,id=pid , status = True)
    if not post.login_require:
        next = post.objects.filter(id__gt=pid , status = True).order_by('id').first()
        pre = post.objects.filter(id__lt=pid  , status = True).order_by('-id').first()
        comments = comment.objects.filter(post = posts.id , approved = True )
        form = commentForm()
        context = {'post':posts , 'next':next , 'pre':pre , 'comments':comments , 'form':form ,}
        return render(request,'blog/blog-single.html' , context)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))

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
