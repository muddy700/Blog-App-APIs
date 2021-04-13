from .models import PostVote
from rest_framework import serializers

class PostVotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostVote
        fields = '__all__'