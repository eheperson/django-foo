
from rest_framework import serializers

from post.models import Post

class PostSerializer(serializers.Serializer):
     title = serializers.CharField(max_length=200)
     content = serializers.CharField(max_length=200)


class PostModelSerializer(serializers.ModelSerializer):
    """ 
        Advantage of using 'serializers.Serializer' instead of 'serializers.ModelSerializer' :
            we do not need to redefine fields on the model which we serialize here

            just define a Meta class inside

            model : Which model will be serialized 
            field : which fields you want to serialize(fields of model)
    """
    class Meta:
         model=Post  
         fields =[
             'user',
             'modified_by',
             'title',
             'content',
             'img',
             'slug',
             'created' 
         ]

class PostModelUpdateCreateSerializer(serializers.ModelSerializer):
    class Meta:
         model=Post  
         fields =[
             'user',
             'modified_by',
             'title',
             'content',
             'img', 
         ]
