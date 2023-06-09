from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_posts, name="posts"),
    path('post/<int:post_id>', views.post_detail, name="post_detail")
]
