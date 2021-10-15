
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


    # def save(self, **kwargs):
    #     """"
    #     we can tampering data before save if we wish

    #     we just need to override that update function as follow 
    #     """
    #     pass

    def create(self, validated_data):
        return Post.objects.create(user =self.context["request"].user, **validated_data)

    def update(self, instance, validated_data):
        """"
        we can tampering data before update if we wish

        we just need to override that update function as follow 
        """
        instance.title = validated_data.get('title', instance.title)
        # instance.content = validated_data.get('content', instance.content)
        instance.content = "enivicivokki" # an example of how to manipulate data before update
        instance.image = validated_data.get('image', instance.image)
        instance.save() # do not forget save after update
        return instance



    # def validate_title(self, value ):
    #     """ 
    #     validation example :

    #     to use validation method we need override it also 
    #     but things are some different for that case 
    #     there is seperated validation functions for each field in model defined in models.py 
    
    #     for example : 

    #         for the validate 'title'  field at the models.Post class  
    #         we need to override the function  'validate_title()' as follow  
        
    #     django_rest, calling validation before update, create vs vs
    #     """
    #     if value == "ehe":
    #         raise serializers.ValidationError("eheni sikmiim, adam gibi bişi yaz. ")
    #     return value

    
    # def validate(self, attrs):
    #     """ 
    #     for example validate_title validates only the title field in the models.Post class

    #     but alternativelly there is another validation function which takes all attributes in the class


    #     and that bitch function is what we are talking about 
    #     """
    #     if attrs["title"] == "enivicivokki":
    #          raise serializers.ValidationError("bu olmaz")
    #     return attrs