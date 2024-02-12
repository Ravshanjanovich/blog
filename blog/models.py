from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF' ,'DRAFT'
        PUBLISHED = 'PB', 'PUBLISHED'




    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    objects = models.Manager()
    published = PublishedManager()




    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]






    def __str__(self) :
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                            related_name='comments')
    name = models.CharField(max_length=70)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]


        def __str__(self):
            return f"Comment by {self.name} on {self.post}"