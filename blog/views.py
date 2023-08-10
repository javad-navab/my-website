from django.shortcuts import render , get_object_or_404
from blog.models import post
import datetime



# Create your views here.
def blog(request ):
    t = datetime.datetime.now()
    posts = post.objects.filter( status=True , published_at__lte=t)
    context = {'posts' : posts }
    return render(request,'blog/blog-home.html' , context)

def blog_single(request , pid):
    posts = post.objects.get(id=pid)
    posts.counted_views=posts.counted_views+1
    posts.save()
    posts = get_object_or_404(post,id=pid , status = True)
    context = {'post':posts }
    return render(request,'blog/blog-single.html' , context)

# def test(request , pid): 
#     # posts = post.objects.get(id=pid)
#     posts = get_object_or_404(post,pk=pid)
#     context = {'post':posts}
#     return render(request,'blog/test.html' , context)