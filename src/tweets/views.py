# -*- coding: utf-8 -*-
from django.shortcuts import render

from .models import Tweet

# Create your views here.


# Create


# Update


# Delete


# Retrieve
def tweet_detail_view(request, id=1):
    obj = Tweet.objects.get(id=id)  # GET from the database
    print(obj)
    context = {
        "object": obj,
    }
    return render(request, 'tweets/detail_view.html', context)


def tweet_list_view(request):
    queryset = Tweet.objects.all()
    for obj in queryset:
    	print(obj.content)
    print(queryset)
    context = {
    	# object_list será renderizado em tweets/list_view.html
        "object_list": queryset
    }
    return render(request, 'tweets/list_view.html', context)
