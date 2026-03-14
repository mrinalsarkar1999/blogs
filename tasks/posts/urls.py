from django.urls import path
from .views import post_list,create_post,delete_post,update_post,get_posts


urlpatterns = [
    path("posts/",post_list),
    path('posts/create/',create_post),
    path("posts/<int:pk>/", get_posts),
    path("posts/update/<int:pk>/",update_post),
    path("posts/delete/<int:pk>/", delete_post),
]