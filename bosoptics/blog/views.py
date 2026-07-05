from django.shortcuts import get_object_or_404, render

from blog.models import Post


def blog_list(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blog/list.html', {'posts': posts})


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    recent = Post.objects.exclude(pk=post.pk).order_by('-created_at')[:3]
    return render(request, 'blog/detail.html', {'post': post, 'recent_posts': recent})
