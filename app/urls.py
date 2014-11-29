from django.conf.urls.defaults import patterns,include,url
from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns=patterns('',url('^$',views.home.post_list),
                        url(r'^post/new$', views.post.post_new),
                        url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post.post_remove),
                        url(r'^post/(?P<pk>[0-9]+)/publish$', views.post.post_publish),
                        url(r'^post/(?P<slug>.*)/edit/$', views.post.post_edit),
                        url(r'^post/(?P<slug>.*)$', views.post.post_detail),
                        url(r'^drafts/$', views.post.post_draft_list),
                        url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
                        url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
                        )
