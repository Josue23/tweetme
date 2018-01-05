from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions

from tweets.models import Tweet
from .serializers import TweetModelSerializer


class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer
    # verifica se o usuário está autenticado
    permission_classes = [permissions.IsAuthenticated]

    # cria o tweet
    def perform_create(self, serializer):
        # pega o usuário logado
        serializer.save(user=self.request.user) # salva o tweet no banco


class TweetListAPIView(generics.ListAPIView):
    # queryset = Tweet.objects.all()
    serializer_class = TweetModelSerializer

    def get_queryset(self, *args, **kwargs):
        # qs = Tweet.objects.all().order_by("-timestamp") # ordena usando timestamp
        qs = Tweet.objects.all().order_by("-pk") # ordena usando pk
        # print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
                )
        return qs