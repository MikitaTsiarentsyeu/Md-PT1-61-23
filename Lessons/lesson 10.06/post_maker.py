import requests
import datetime

def get_posts():
    response = requests.get("http://127.0.0.1:8000/api/post/")
    if response.status_code == 200:
        posts = response.json()
        return posts
    else:
        return []
    
print(get_posts())

def create_post(title, content, author):
    post_data = {
        "title": title,
        "content": content,
        "issued": str(datetime.datetime.now()),
        "author": author
    }
    response = requests.post("http://127.0.0.1:8000/api/post/", json=post_data)
    if response.status_code == 201:
        post = response.json()
        return post
    
new_post = create_post("new post from post_maker", "test", "test@te.st")
print(new_post)
