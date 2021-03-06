# -*- coding: utf-8 -*- 

from django.shortcuts import render
from django.utils import timezone
from datetime import datetime
from .models import Post, Profile
from django.utils.dateparse import parse_date
from django.http.response import HttpResponse
from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView

from django.contrib.auth.models import User

import os
import time

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
	user_id = serializers.CharField(source='get_user_id') 

	class Meta:
		model = Post
		fields = ('id', 'user_id', 'reservation_date', 'authorName', 'title', 'contents', 'question', 'introduction', 'link', 'profile_image_link', 'book', 'publisher', 'published_date' )

class PoetSerializer(serializers.ModelSerializer):
	author_name = serializers.CharField(source='get_user_full_name')
	user_id = serializers.CharField(source='get_user_id')

	class Meta:
		model = Profile
		fields = '__all__'

class today_api(GenericAPIView, mixins.ListModelMixin):
    today = timezone.localtime(timezone.now())
    queryset = Post.objects.filter(reservation_date__year=today.year, reservation_date__month=today.month, reservation_date__day=today.day)
	# today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
	# today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
	# queryset = Post.objects.filter(reservation_date__range=(today_min, today_max)).order_by('reservation_date')
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class poet_api(GenericAPIView, mixins.ListModelMixin):
	queryset = Profile.objects.filter(user__groups__name__in=['시인']).order_by('day')
	serializer_class = PoetSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

class poem_api(GenericAPIView, mixins.ListModelMixin):
	serializer_class = PostSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def get_queryset(self):
		queryset = Post.objects.all()
		poem_id = self.request.query_params.get('id', None)
		user_id = self.request.query_params.get('user_id', None)
		reservation_date = self.request.query_params.get('reservation_date', None)
		if poem_id is not None:
			queryset = queryset.filter(id=poem_id)
		if user_id is not None:
			queryset = queryset.filter(author__username=user_id)
		if reservation_date is not None:
			reservation_parsed_date = parse_date(reservation_date)
			queryset = 	queryset.filter(reservation_date__year=reservation_parsed_date.year, reservation_date__month=reservation_parsed_date.month, reservation_date__day=reservation_parsed_date.day)

		return queryset.order_by('-reservation_date')



class today_api_test(GenericAPIView, mixins.ListModelMixin):
	today = datetime.utcnow()
	queryset = Post.objects.filter(reservation_date__year=today.year, reservation_date__month=today.month, reservation_date__day=today.day)
	serializer_class = PostSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)
