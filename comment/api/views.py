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

# Mixins
# Mixin'ler bir view a bazı davranışlar kazandırır
from rest_framework.mixins import (
    DestroyModelMixin, # DestroyModelMixin destroy() diye bir fonksiyon sağlar
    UpdateModelMixin, # UpdateModelMixin update() diye bir fonksiyon sağlar
    RetrieveModelMixin, # RetrieveModelMixin retrieve() diye bir fonksiyon sağlar
    CreateModelMixin, # CreateModelMixin create() diye bir fonksiyon sağlar
)

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

class CommentListCreateAPIView(
    ListAPIView,
    CreateModelMixin
):
    # queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    pagination_class = CommentPagination
    def get_queryset(self):
        queryset = Comment.objects.filter(parent=None) 
        query = self.request.GET.get("q") #localhost:8000/api/comment/list?q=12 - id si 12 olan posta ait yorumları listelemek için
        if query:
            queryset = queryset.filter(post="query")
        return queryset 

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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

class CommentEditAPIView(
    UpdateAPIView, 
    RetrieveAPIView, 
    UpdateModelMixin, 
    RetrieveModelMixin,
    DestroyModelMixin
):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteUpdateSerializer 
    lookup_field = 'pk'
    permission_classes = [IsOwner]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    