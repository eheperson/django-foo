#
#
# $ ./manage.py shell < shell.py 
# it is same with drop into the Django shell : $python manage.py shell

from post.models import Post
from post.api.serializers import PostSerializer 



obj = Post.objects.first() 
print(obj.title) 



new = PostSerializer(obj)
print(new.data)  



data = {
    "title" : "enivicivokki",
    "content" : "ehhe",
}
# # that will cause an error because of the required files 
# data = {
#     "title" : "enivicivokki",
# }
new = PostSerializer(data=data)

if new.is_valid():
    new.save()
else:
    print(new.errors)


######## Delete and Update by serializers
from post.api.serializers import PostModelSerializer
from post.models import Post 

obj = Post.objects.get(id =1)
print(obj.title)

data = {"title":"eeeee", "content":"eeeeeee"}

temp = PostModelSerializer(obj, data =data)

# to check is new created object valid
print(temp.is_valid())
 
#to check if any error
print(temp.errors)

# to update object
data2 = {"title":"eeeee222", "content":"eeeeeee222"}
temp = PostModelSerializer(obj, data =data2)

#to delete object
obj.delete()