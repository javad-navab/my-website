from django.shortcuts import render , get_object_or_404
from blog.models import post
import datetime



# Create your views here.
def blog(request ):
    t = datetime.datetime.now()
    posts = post.objects.filter(published_at__lte=t , status=True)
    context = {'posts' : posts }
    return render(request,'blog/blog-home.html' , context)

def blog_single(request , pid):
    # counter=post.objects.get(id=pid)
    # counter.counted_views=counter.counted_views+1
    # counter.save()
    posts = post.objects.get(id=pid)
    posts.counted_views=posts.counted_views+1
    posts.save()
    posts = get_object_or_404(post,pk=pid)
    context = {'post':posts }
    return render(request,'blog/blog-single.html' , context)

# def test(request , pid): 
#     # posts = post.objects.get(id=pid)
#     posts = get_object_or_404(post,pk=pid)
#     context = {'post':posts}
#     return render(request,'blog/test.html' , context)