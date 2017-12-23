from django.db import models
from django.utils import timezone

class Post(models.Model):
    reservation_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    contents = models.TextField()
    question = models.TextField()
    profile_link = models.CharField(max_length=200, blank=True)
    external_author = models.CharField(max_length=20, blank=True)
    book = models.CharField(max_length=100, blank=True)
    publisher = models.CharField(max_length=100, blank=True)
    published_date = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message
