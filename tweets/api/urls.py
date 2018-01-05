# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.generic.base import RedirectView

from .views import (
    TweetListAPIView,
    TweetCreateAPIView
    )

urlpatterns = [

    # CBV - Class Based View
    url(r'^$', TweetListAPIView.as_view(), name='list'), # /api/tweet/ first endpoint
    url(r'^create/$', TweetCreateAPIView.as_view(), name='create'), # /api/tweet/create/
]
