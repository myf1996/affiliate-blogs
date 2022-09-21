from django.urls import include, re_path

from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    re_path('^$', views.home, name='home'),
    re_path('^tag/(?P<slug>[A-Za-z0-9-_]+)$', views.tagList, name='blog-list'),
    re_path('^category/(?P<slug>[A-Za-z0-9-_]+)$', views.categoryList, name='blog-list'),
    re_path('^category/(?P<cat_slug>[A-Za-z0-9-_]+)/(?P<blog_slug>[A-Za-z0-9-_]+)$', views.blogDetail, name='blog-detail')
    # re_path('blog', views.blogSingle, name='blogSingle'),
    # re_path('^blog$', views.blogSingle, name='blogSingle'),
    # url('^about-us/$', views.about_us, name='about-us'),
    # url('^services/$', views.services, name='services'),
    # url('^contact-us/$', views.contact_us, name='contact_us'),
]