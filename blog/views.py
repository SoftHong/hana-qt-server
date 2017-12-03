from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.http.response import HttpResponse
from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def blog_page(request):
	post_list = Post.objects.all()
	return HttpResponse('Hello!' + post_list[0].title)

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'

class blog_api(GenericAPIView, mixins.ListModelMixin):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)