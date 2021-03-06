# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    ListView,
    UpdateView,
    )

from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
# importa o model para fazer query a partir da views.py
from .models import Tweet


# Create

class TweetCreateView(FormUserNeededMixin, CreateView):

    # queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html' # "POST /tweet/create/ HTTP/1.1" 302 0
    # fields = ['user', 'content']
    # success_url = "/tweet/create/" # "GET /tweet/create/ HTTP/1.1" 200 351
    # success_url = reverse_lazy("tweet:detail")
    # success_url = "/" # redireciona para a url home # "GET / HTTP/1.1" 200 1431
    # login_url = '/admin/'
    # redirect_field_name = 'redirect_to'


# def tweet_create_view(request):
#     form = TweetModelForm(request.POST or None)

#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.user = request.user
#         instance.save()

#     context = {
#         "form": form
#     }
#     return render(request, 'tweets/create_view.html', context)


# Update

# posso usar LoginRequiredMixin ou FormUserNeededMixin
class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    # success_url = "/tweet/"


# Delete

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = "tweets/delete_confirm.html"

    # namespace: tweet - feito no tweetme/urls.py
    # nome da url: list
    # reverse() traduz para /tweet/list/
    success_url = reverse_lazy("tweet:list") # reverse() # /tweet/



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
    # queryset = Tweet.objects.all()
    # chama automaticamente tweet_list.html -app_list
    # template_name = 'tweets/list_view.html'

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        # queryset = super(CLASS_NAME, self).get_queryset()
        # queryset = queryset # TODO
        # print(self.request.GET)
        query = self.request.GET.get("q", None)
        # print("query: {}".format(query))
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
                )
        return qs

    
    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = TweetModelForm() # /tweets/tweet_list.html
        context['create_url'] = reverse_lazy('tweet:create') # /tweets/tweet_list.html
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
