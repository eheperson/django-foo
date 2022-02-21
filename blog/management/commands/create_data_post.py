#  python manage.py create_data_post post 
#
# run those codes on shell if command does not work
import json
from blog.models import Post

with open('posts.json') as f:
    post_json = json.load(f)

for post in post_json:
    post = Post(title=post['title'], content=post['content'], author_id=post['user_id'])
    post.save()

exit()