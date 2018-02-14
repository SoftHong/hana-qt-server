from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=200, blank=True)
    image_link = models.CharField(max_length=200, blank=True)
    introduction = models.TextField()
    day = models.DecimalField(max_digits=7, decimal_places=0, default=0)

    def __str__(self):
        return self.user.username

    def get_user_full_name(self):
        fullName = ""
        if self.user.last_name != "":
            fullName += self.user.last_name
        if self.user.first_name != "":
            fullName += self.user.first_name
        return fullName
    
    def get_user_name(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class ExternalProfile(models.Model):
    author = models.CharField(max_length=20)
    link = models.CharField(max_length=200, blank=True)
    image_link = models.CharField(max_length=200, blank=True)
    introduction = models.TextField()

    def __str__(self):
        return self.author

class Post(models.Model):
    reservation_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    contents = models.TextField()
    question = models.TextField()
    external_profile = models.ForeignKey(ExternalProfile, null=True, blank=True)
    book = models.CharField(max_length=100, blank=True)
    publisher = models.CharField(max_length=100, blank=True)
    published_date = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_user_full_name(self):
        fullName = ""
        if self.author.last_name != "":
            fullName += self.author.last_name
        if self.author.first_name != "":
            fullName += self.author.first_name
        if self.external_profile:
            fullName = ExternalProfile.objects.get(author=self.external_profile).author
        return fullName

    def get_user_introduction(self):
        introduction = Profile.objects.get(user=self.author).introduction
        if self.external_profile:
            introduction = ExternalProfile.objects.get(author=self.external_profile).introduction
        return introduction

    def get_user_link(self):
        link = Profile.objects.get(user=self.author).link
        if self.external_profile:
            link = ExternalProfile.objects.get(author=self.external_profile).link
        return link

    def get_user_image_link(self):
        image_link = Profile.objects.get(user=self.author).image_link
        if self.external_profile:
            image_link = ExternalProfile.objects.get(author=self.external_profile).image_link
        return image_link

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message
    