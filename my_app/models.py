from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE, related_name='posts')
    content = models.CharField(max_length=500)
    picture = models.ImageField(upload_to='post_pictures/' , blank=True , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
                return f"{self.user.username} - {self.created_at} - {self.content}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    comment_text = models.TextField( max_length=500 , blank=True , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self  ,):
        return f'Comment on {self.post} by {self.user.username}'
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Like on {self.post.content}'
    
class Share(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_shares')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_shares')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} shared {self.post}"

    
