from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Post
import json

# Get all posts
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        data = []
        for post in posts:
            data.append({
                'id':post.id,
                'title':post.title,
                'slug':post.slug,
                'content':post.content,
                'author':post.author,
                'created_at':post.created_at,
            })
        return JsonResponse(data,safe=False)

# Create a post    
@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        user = User.objects.get(id=body['author'])
        post = Post.objects.create(
            title = body['title'],
            slug = body['slug'],
            content = body['content'],
            author = user,
        )
        data = {
            'id':post.id,
            'title':post.title,
            'content':post.content,
        }

        return JsonResponse(data)

# Get a single post
def get_posts(request,pk):
    if request.method == 'GET':
        post = Post.objects.get(id=pk)
        data = {
            'id':post.id,
            'title':post.title,
            'slug':post.slug,
            'content':post.content,
            'author':post.author.username,
        }

        return JsonResponse(data)
    
# Update a post
def update_post(request,pk):
    if request.method == 'PUT':
        post = Post.objects.get(id=pk)
        body = json.loads(request.body)
        post.title = body.get('title',post.title)
        post.content = body.get('content',post.content)

        post.save()

        return JsonResponse({"message":"Post Updated Succesfully"})
    
# Delete a post
def delete_post(request,pk):
    if request.method == 'DELETE':
        post = Post.objects.get(id=pk)
        post.delete()

        return JsonResponse({"message":"Post Deleted"})