

from blog.models import Post
from django.contrib.auth.models import User

# get all users in User data table
users = User.objects.all()

# get first user from User data table
firstUser = User.objects.first()

# get last user from User data table
lastUser = User.objects.last()

# filtering by username
ehePersonUser = User.objects.filter(username='ehePerson')

# get the first result of filtering query
ehePersonUserFirst = User.objects.filter(username='ehePerson').first()

# user attributes
print(" User ID : ", ehePersonUserFirst.id)
print(" User ID : ", ehePersonUserFirst.pk) # via primary key = id 

# get by id
user = User.objects.get(id=1)
# Create new post
posts = Post.objects.all() # will return empty
print("Posts : ", posts)

post1 = Post(title="Post 1", content="Content of first post", author=user)
posts = Post.objects.all() # will return empty
print("Posts : ", posts)

post1.save()
posts = Post.objects.all() # will not return empty
print("Posts : ", posts)

# Create and save another post
user2 = User.object.filter(username="JaneDoe").first()
# post1 = Post(title="Post 2", content="Content of second post", author=user2)
post2 = Post(title="Post 2", content="Content of second post", author_id=user2.id)
post2.save()


posts = Post.objects.all() # will not return empty
print("Posts : ", posts)
print("First Post : ", posts.first())
print("First Post - Posted Date : ", posts.first().date_posted)
print("First Post - Author : ", posts.first().author)
print("First Post - Author email: ", posts.first().author.email)

# All the posts user created : 
user = User.objects.get(id=1)
posts = user.post_set # reverse foreignkey relation
# create a new post via reverse relation
user.post_set.create(title="Post 3", content="Content of second post") # we do not need specify autfor in thos case
# and we don not need run save() method, django saves it automatically in that case.

# Now check the posts
print("Posts : ", Post.objects.all())

# interact by user profiles
from django.contrib.auth.models import User
user = User.objects.filter(username='eheperson').first()
print("user profile :", user.profile)
print("user profile image :", user.profile.img)
print("user profile image width :", user.profile.img.width)
print("user profile image height:", user.profile.img.height)
print("user profile image path url:", user.profile.img.url)


# Paginators
from django.core.paginator import Paginator
posts = ['1', '2', '3', '4', '5']
p = Paginator(posts, 2)
p.num_pages 

for page in p.page_range:
    print(page)

p1 = p.page(1)
print(p1)
print(p1.number)
print(p1.object_list)
print(p1.has_previous())
print(p1.has_next())
print(p1.next_page_number())
 

