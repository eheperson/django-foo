from rest_framework.generics import (ListAPIView, 
                                     RetrieveAPIView, 
                                     UpdateAPIView, 
                                     RetrieveUpdateAPIView, 
                                     DestroyAPIView,
                                     CreateAPIView)

from rest_framework.settings import perform_import
from .serializers import PostSerializer, PostModelSerializer, PostModelUpdateCreateSerializer 
from post.models import Post

from rest_framework.permissions import (IsAdminUser, IsAuthenticated)

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 

class PostListAPIViewModel(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all() 
    serializer_class = PostModelSerializer 

    # which field do you want to go details of model  
    # default : lookup_field = 'pk'
    lookup_field = 'slug' 

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all() 
    serializer_class = PostModelUpdateCreateSerializer 
    lookup_field = 'slug' 

    def perform_update (self, serializer ):
        serializer.save(modified_by = self.request.user)

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all() 
    serializer_class = PostModelSerializer 
    lookup_field = 'slug' 

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all() 
    serializer_class = PostModelUpdateCreateSerializer 
    permission_classes =[IsAuthenticated]
    
    def perform_create(self, serializer ):
        serializer.save(user = self.request.user)