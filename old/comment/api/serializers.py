from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)

from comment.models import ( 
    Comment, 
    User,
    Post
)

class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['created',] # do not forget difference between 'fields' and 'exclude' bitch. 
                              # You have to remember it until tomorrow morning.

    def validate(self, attrs):
        if(attrs["parent"]):
            if attrs["parent"].post != attrs["post"]:
                raise serializers.ValidationError("Something went wrong!")

        return attrs

# class CommentChildSerializer(ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        # exclude = ['password']
        # or :
        fields = ('first_name', 'last_name', 'id', 'email')

class PostCommentSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'id')

class CommentListSerializer(ModelSerializer):
    replies = SerializerMethodField()
    user = UserSerializer()
    post = PostCommentSerializer()
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 1 #try this bitch

    def get_replies(self, obj):
        if obj.any_children:
            # do not use this shity way
            # return CommentChildSerializer(obj.children(), many=True).data
            return CommentListSerializer(obj.children(), many=True).data


class CommentDeleteUpdateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields=[
            'content'
        ]