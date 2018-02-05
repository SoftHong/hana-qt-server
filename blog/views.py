from django.shortcuts import render
from django.utils import timezone
from datetime import date
from tzlocal import get_localzone # pip install tzlocal
from .models import Post, Profile
from django.http.response import HttpResponse
from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView

from django.contrib.auth.models import User

def post_list(request):
    posts = Post.objects.filter(reservation_date__gte=timezone.now()).order_by('reservation_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def blog_page(request):
	post_list = Post.objects.all()
	return HttpResponse('Hello!' + post_list[0].title)

class PostSerializer(serializers.ModelSerializer):
		authorName = serializers.CharField(source='get_user_full_name')
		introduction = serializers.CharField(source='get_user_introduction')
		link = serializers.CharField(source='get_user_link')
		profile_image_link = serializers.CharField(source='get_user_image_link')

		class Meta:
			model = Post
			fields = ('id', 'reservation_date', 'authorName', 'title', 'contents', 'question', 'introduction', 'link', 'profile_image_link', 'book', 'publisher', 'published_date' )


class today_api(GenericAPIView, mixins.ListModelMixin):
	local_tz = get_localzone()
	timezone.activate(local_tz)
	today = timezone.localtime(timezone.now())
	queryset = Post.objects.filter(reservation_date__year=today.year, reservation_date__month=today.month, reservation_date__day=today.day)
	serializer_class = PostSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

