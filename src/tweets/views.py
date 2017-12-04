# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import DetailView, ListView

# importa o model para fazer query a partir da views.py
from .models import Tweet


# Create


# Update


# Delete


# Retrieve
# CBV
class TweetDetailView(DetailView):
    # chama automaticamente tweet_detail.html - app_detail

    # template_name = 'tweets/detail_view.html'
    queryset = Tweet.objects.all()

    def get_object(self):
        return Tweet.objects.get(id=1)

# CBV
class TweetListView(ListView):
    # chama automaticamente tweet_list.html -app_list

    # template_name = 'tweets/list_view.html'
    queryset = Tweet.objects.all()

    
    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        # context["another_list"] = Tweet.objects.all()
        # print(context)
        return context
    

# FBV
# def tweet_detail_view(request, id=1):
#     obj = Tweet.objects.get(id=id)  # GET from the database
#     print("Objeto: {}".format(obj))
#     context = {
#         "object": obj,
#     }
#     return render(request, 'tweets/detail_view.html', context)

# FBV
# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     print("\n\nTipo da queryset: {} ".format(type(queryset)))
#     for obj in queryset:
#     	print(obj.content)
#     print(queryset)
#     context = {
#     	# object_list será renderizado em tweets/list_view.html
#         "object_list": queryset
#     }
#     return render(request, 'tweets/list_view.html', context)
