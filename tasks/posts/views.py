from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Post,Tag
import json

# Get all posts
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all().order_by('-created_at')
        data = []
        for post in posts:
            data.append({
                'id': post.id,
                'title': post.title,
                'slug': post.slug,
                'content': post.content,
                'author': post.author.username, # Send username string
                'created_at': post.created_at,
                'cover_image': post.cover_image.url if post.cover_image else None,
                'tags': [{'id': t.id, 'name': t.name} for t in post.tags.all()] # Extract tags
            })
        return JsonResponse(data, safe=False)

# Create a post    
@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        # 1. Use request.POST instead of json.loads(request.body)
        title = request.POST.get('title')
        slug = request.POST.get('slug')
        content = request.POST.get('content')
        author_id = request.POST.get('author')
        tags_raw = request.POST.get('tags', '') # Expecting comma-separated string

        # 2. Get the image from request.FILES
        cover_image = request.FILES.get('cover_image')

        try:
            user = User.objects.get(id=author_id)
            # Create the post object
            post = Post.objects.create(
                title=title,
                slug=slug,
                content=content,
                author=user,
                cover_image=cover_image # Django handles the file saving
            )

            # 3. Handle Tags manually
            if tags_raw:
                tag_list = [t.strip() for t in tags_raw.split(',') if t.strip()]
                for tag_name in tag_list:
                    # Get or create the tag so it doesn't fail if it exists
                    tag_obj, created = Tag.objects.get_or_create(name=tag_name)
                    post.tags.add(tag_obj)

            data = {
                'id': post.id,
                'title': post.title,
                'message': "Post created successfully with image and tags!"
            }
            return JsonResponse(data)
            
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Method not allowed'}, status=405)

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
@csrf_exempt
def update_post(request,pk):
    if request.method == 'PUT':
        post = Post.objects.get(id=pk)
        body = json.loads(request.body)
        post.title = body.get('title',post.title)
        post.content = body.get('content',post.content)

        post.save()

        return JsonResponse({"message":"Post Updated Succesfully"})
    
# Delete a post
@csrf_exempt
def delete_post(request,pk):
    if request.method == 'DELETE':
        post = Post.objects.get(id=pk)
        post.delete()

        return JsonResponse({"message":"Post Deleted"})