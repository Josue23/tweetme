from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()

class UserDisplaySerializer(serializers.ModelSerializer):
    # SerializerMethodField - read-only field
    follower_count = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'follower_count',
            # 'email'
        ]
    
    def get_follower_count(self, obj): # obj éa instancia de User
        # print(obj.username)
        return 0