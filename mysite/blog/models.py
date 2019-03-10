from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BlogArtcles(models.Model):
    title = models.CharField(max_length=300)  #1规定了字段 title 的属性为CharField（）类型，并说明最大值
    author = models.ForeignKey(User, related_name="blog_posts",on_delete=models.CASCADE,) #2通过字段 author 规定了博客文章和作者之间的关系，
    #ForeignKey（）反应“一对多”关系，类User就是BlogArtcles的对应对象，related_name="blog_posts"的作用是允许通过类User反向查询到BlogArtcles
    body = models.TextField()  #大文本。默认对应的form标签是textarea。
    publish = models.DateTimeField(default=timezone.now)


    class Meta:  #3 通过 ordering = ("-publish",)规定BlogArtcles实例对象显示顺序，即按照publish字段值的倒序显示
        ordering = ("-publish",)

    def __str__(self):
        return self.title



