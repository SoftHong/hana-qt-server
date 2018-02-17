"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from blog.views import blog_page, today_api, poet_api, poem_api, today_api_test

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'^rest-api/', include('rest_framework.urls')),
#    url(r'^rest-swagger/', include('rest_framework_swagger.urls')),

    # blog
    url(r'^blog/', blog_page),

    # rest
    url(r'^api/today/', today_api.as_view()),
    url(r'^api/poet/', poet_api.as_view()),
    url(r'^api/poem/(?:title-(?P<title>\d+)/)?$', poem_api.as_view()),
    url(r'^api/test/', today_api_test.as_view()),
]
