from django.shortcuts import render, get_object_or_404
from .models import Blogs, Category
from django.db.models import Q
from django.http import HttpResponse

def post_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Blogs.objects.filter(status='public', category=category).order_by('-created_at')
    categories = Category.objects.all()

    context = {
        'category': category,
        'category_posts': posts,
        'categories': categories,
    }
    return render(request, 'post_by_category.html', context)


def blog_view(request,slug):
    single_post=get_object_or_404(Blogs, slug=slug, status='public')
    categories=Category.objects.all()
    context={
        'single_post':single_post,
        'categories':categories,
    }
    return render(request, 'blog_view.html', context)


def search(request):
    keyword = request.GET.get('keyword', '').strip()
    blogs = Blogs.objects.none()  # Default to empty queryset
    
    if keyword:
        blogs = Blogs.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='public')
    
    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'base/search.html', context)
