import os

# we can get a list of all of the snippets:
os.system("http http://127.0.0.1:8000/snippets/")

# we can get a particular snippet by referencing its id:
os.system("http http://127.0.0.1:8000/snippets/2/")
