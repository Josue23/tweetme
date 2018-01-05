from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer
from tweets.models import Tweet # from ..models import Tweet

class TweetModelSerializer(serializers.ModelSerializer):
    # não permite alterar dados do usuário
    # permite alterar somente o conteúdo
    user = UserDisplaySerializer(read_only=True) # read_only ou write_only # foreign key
    class Meta:
        model = Tweet
        fields = [
            'user',
            'content',
            'timestamp'
        ]