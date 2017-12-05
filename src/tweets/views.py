# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

# importa o model para fazer query a partir da views.py
from .models import Tweet


# Create


# Update


# Delete


# Retrieve
# CBV
class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    # chama automaticamente tweet_detail.html - app_detail

    # template_name = 'tweets/detail_view.html'

    # def get_object(self):
    #     print(self.kwargs)
    #     pk = self.kwargs.get("pk")
    #     # pk = self.kwargs["pk"]
    #     obj = get_object_or_404(Tweet, pk=pk)
    #     # return Tweet.objects.get(id=pk) # substitui por return obj
    #     return obj

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
def tweet_detail_view(request, pk=None): # pk == id
    obj = Tweet.objects.get(pk=pk)  # GET from the database
    obj = get_object_or_404(Tweet, pk=pk)
    print("Objeto: {}".format(obj))
    context = {
        "object": obj,
    }
    return render(request, 'tweets/detail_view.html', context)

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
