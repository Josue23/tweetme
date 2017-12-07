# -*- coding: utf-8 -*-
# from django.contrib import admin

# from django.conf import settings
# from django.conf.urls.static import static
from django.conf.urls import url
from .views import (
    # TweetListView, 
    TweetCreateView,
    TweetDetailView,
    TweetListView
    # tweet_detail_view, 
    ) # tweet_list_view,

urlpatterns = [
    # FBV - Function Based View
    # url(r'^$', tweet_list_view, name='list'),
    # url(r'^1/$', tweet_detail_view, name='detail'),
    # url(r'^admin/', admin.site.urls),

    # CBV - Class Based View
    url(r'^$', TweetListView.as_view(), name='list'), # /tweet/ - vem de /tweetme/urls.py
    url(r'^create/$', TweetCreateView.as_view(), name='create'), # /tweet/create/ - vem de /tweetme/urls.py
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), # /tweet/1/(?P<pk>\d+)]
]
