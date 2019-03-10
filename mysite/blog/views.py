from django.shortcuts import render, get_object_or_404
from .models import BlogArtcles

def blog_title(request):
    blogs = BlogArtcles.objects.all()
    return render(request, 'blog/titles.html', {'blogs':blogs})


def blog_article(request,article_id):
    #article = BlogArtcles.objects.get(id=article_id) 之前的
    article = get_object_or_404(BlogArtcles, id=article_id)
    pub = article.publish
    return render(request, "blog/content.html",{"article":article, "publish":pub})