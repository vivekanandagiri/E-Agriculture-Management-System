from multiprocessing import context
from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
# Create your views here.


def news(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 6)  # Show 6 posts per page

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    context = {'posts': posts}
    return render(request, 'news.html', context)

#def viewnews(request,slug):
    #post=Post.objects.get(slug=slug)
    ##context={'post':post}
    #return render(request,'detailnews.html',context)
from django.shortcuts import render, get_object_or_404
from .models import Post

def viewnews(request, slug):
    post = get_object_or_404(Post, slug=slug)
    recent_posts = Post.objects.order_by('-created')[:5]  # Fetch the 5 most recent posts
    
    context = {
        'post': post,
        'recent_posts': recent_posts,
    }
    return render(request, 'detailnews.html', context)
