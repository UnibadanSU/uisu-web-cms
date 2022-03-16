from rest_framework import serializers

from news.models import Post, Profile, Executive, Tag

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class ExecutiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executive
        fields = '__all__'