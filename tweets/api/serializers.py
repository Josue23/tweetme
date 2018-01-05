from django.utils.timesince import timesince
from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer
from tweets.models import Tweet # from ..models import Tweet

class TweetModelSerializer(serializers.ModelSerializer):
    # não permite alterar dados do usuário
    # permite alterar somente o conteúdo
    user = UserDisplaySerializer(read_only=True) # read_only ou write_only # foreign key
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = [
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince',
        ]
    
    # https://docs.python.org/3/library/datetime.html?highlight=strftime#strftime-and-strptime-behavior
    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d, %I:%M %p")
    
    def get_timesince(self, obj):
        return timesince(obj.timestamp) + " ago"