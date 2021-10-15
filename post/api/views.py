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

#custom permissions
from .permissions import IsOwner

from rest_framework.filters import SearchFilter, OrderingFilter

from .paginations import PostPagination


class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer 
    # queryset = Post.objects.all()

    filter_backends = [SearchFilter] #we will apply search filter, that is the why we used SearchFilter
    
    search_fields = ['title'] # We specify how we will search.
    # to use search_fields : 
        # http://127.0.0.1:8000/api/post/list?search=ehe
        #
        # that api end poind will return all Posts have "ehe" string in their title
    # another example : 
    #     search_fields = ['title', 'content'] # We specify how we will search.
    #
    #     if we go to :
    #         http://127.0.0.1:8000/api/post/list?search=ehe
    #
    #     that api end poind will return all Posts have "ehe" string in their title or in their content




    # filter_backends = [SearchFilter, OrderingFilter] #we will apply search filter, that is the why we used SearchFilter
    # if we use OrderingFilter class : 
    #     and visit the url : 
    #         http://127.0.0.1:8000/api/post/list?search=ehe&ordering=title 

    #     that api end poind will return all Posts have "ehe" string in their title or in their content

    #     and will order them according to their titles (maybe alphabetic order ???)

    #         http://127.0.0.1:8000/api/post/list?search=ehe&ordering=user 

    #     ordering will be according to the user field at the Post

    #         http://127.0.0.1:8000/api/post/list?search=ehe&ordering=-user 

    #     ordering will be reverse according to the user field at the Post
    #      because of the -


    # that is the example of how we use pagination_class (by overriding)
    pagination_class = PostPagination

    def get_queryset(self):
        """ 
            filtering query set 

            purpose is query the post which are not draft
            (do not show drafts, list only posts)
        """
        queryset = Post.objects.filter(draft=False)
        return queryset

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
    permission_classes = [IsOwner]

    def perform_update (self, serializer ):
        serializer.save(modified_by = self.request.user)

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all() 
    serializer_class = PostModelSerializer 
    lookup_field = 'slug' 
    permission_classes = [IsOwner]


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all() 
    serializer_class = PostModelUpdateCreateSerializer 
    permission_classes =[IsAuthenticated] # if the user is authenticated
    # permission_classes =[IsAuthenticated, IsAdminUser] # if the user is authenticated and Admin (not or, and )

    # we will override a rest_framework serializers create func
    # so we do not need to perform_create here
    # check the serializers.py PostModelUpdateCreateSerializer class
    # edit : uncommented because crete function is commented at serializers.PostModelUpdateCreateSerializer
    def perform_create(self, serializer ):
        serializer.save(user = self.request.user)