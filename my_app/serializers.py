
from rest_framework import serializers
from .models import Post, Like, Comment, Share
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Like
        fields = ['id', 'user', 'created_at' , 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'user', 'comment_text', 'created_at' , 'updated_at']

class ShareSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Share
        fields = ['id', 'user', 'created_at' , 'updated_at']

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post_likes = serializers.SerializerMethodField()
    post_comments = serializers.SerializerMethodField()
    post_shares = serializers.SerializerMethodField()
    
    def get_post_likes(self, obj):
        likes = getattr(obj, '_prefetched_likes', obj.post_likes.all())
        return LikeSerializer(likes, many=True).data
    
    def get_post_comments(self, obj):
        comments = getattr(obj, '_prefetched_comments', obj.post_comments.all())
        return CommentSerializer(comments, many=True).data
    
    def get_post_shares(self, obj):
        shares = getattr(obj, '_prefetched_shares', obj.post_shares.all())
        return ShareSerializer(shares, many=True).data
    
    def create(self, validated_data):
        user = self.context['request'].user
        return Post.objects.create(user = user, **validated_data)
    
    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'picture', 'created_at', 'updated_at', 'post_likes', 'post_comments', 'post_shares']
