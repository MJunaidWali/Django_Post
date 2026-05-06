from my_app.models import Post, Like, Comment, Share
from my_app.serializers import PostSerializer
from rest_framework.generics import CreateAPIView, ListAPIView , RetrieveAPIView, UpdateAPIView, DestroyAPIView
from django.db.models import Prefetch
from rest_framework.permissions import IsAuthenticatedOrReadOnly , IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class PostListView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get_queryset(self):
        queryset = Post.objects.all().select_related('user').prefetch_related(
            Prefetch('post_likes', queryset=Like.objects.select_related('user'), to_attr='_prefetched_likes'),
            Prefetch('post_comments', queryset=Comment.objects.select_related('user'), to_attr='_prefetched_comments'),
            Prefetch('post_shares', queryset=Share.objects.select_related('user'), to_attr='_prefetched_shares'),
        ).order_by('created_at')
        return queryset

class PostCreateView(CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class PostRetrieveView(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
class PostUpdateView(UpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class PostDeleteView(DestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]