from django.shortcuts import render
from django.utils import timezone
from datetime import date
from .models import Post, Profile
from django.http.response import HttpResponse
from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView

from django.contrib.auth.models import User

def post_list(request):
    posts = Post.objects.order_by('reservation_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def blog_page(request):
	post_list = Post.objects.all()
	return HttpResponse('Hello!' + post_list[0].title)

class PostSerializer(serializers.ModelSerializer):
		# authorName = serializers.SerializerMethodField('get_user_full_name')
		authorName = serializers.CharField(source='get_user_full_name')
		introduction = serializers.CharField(source='get_user_introduction')
		link = serializers.CharField(source='get_user_link')

		# introduction = serializers.SerializerMethodField('get_user_introduction')
		# link = serializers.SerializerMethodField('get_user_link')

		class Meta:
			model = Post
			fields = ('id', 'reservation_date', 'authorName', 'title', 'contents', 'question', 'introduction', 'link', 'book', 'publisher', 'published_date' )
			# fields = '__all__'

		# def get_user_full_name(self, obj):
		# 	request = self.context['request']
		# 	user = request.user
		# 	name = ""
		# 	if user.last_name != "":
		# 		name = user.last_name

		# 	if user.first_name != "":
		# 		name = name + user.first_name
		# 	return name

		# def get_user_introduction(self, obj):
		# 	request = self.context['request']
		# 	profile = request.user.profile
		# 	return profile.introduction
		
		# def get_user_link(self, obj):
		# 	request = self.context['request']
		# 	profile = request.user.profile
		# 	return profile.link


class today_api(GenericAPIView, mixins.ListModelMixin):
	# queryset = Post.objects.all()
	# queryset = Post.objects.filter(reservation_date__lte=timezone.now()).order_by('reservation_date')

	queryset = Post.objects.filter(reservation_date__date=date.today()).order_by('reservation_date')
	serializer_class = PostSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

