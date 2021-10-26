from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveAPIView
)

from comment.models import Comment
from comment.api.serializers import (
    CommentCreateSerializer,
    CommentListSerializer,
    CommentDeleteUpdateSerializer,
)
from comment .api.permissions import IsOwner

from .paginations import CommentPagination


class CommentCreateAPIView(CreateAPIView):
     queryset = Comment.objects.all()
     serializer_class = CommentCreateSerializer

     def perform_create(self,serializer):
         serializer.save(user = self.request.user) 

class CommentListAPIView(ListAPIView):
    # queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    pagination_class = CommentPagination
    def get_queryset(self):
        queryset = Comment.objects.filter(parent=None) 
        query = self.request.GET.get("q") #localhost:8000/api/comment/list?q=12 - id si 12 olan posta ait yorumları listelemek için
        if query:
            queryset = queryset.filter(post="query")
        return queryset 

class CommentDeleteAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteUpdateSerializer 
    lookup_field = 'pk'
    permission_classes = [IsOwner]

class CommentUpdateAPIView(UpdateAPIView, RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteUpdateSerializer 
    lookup_field = 'pk'
    permission_classes = [IsOwner]