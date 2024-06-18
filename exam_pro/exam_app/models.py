from django.db import models
from django.contrib.auth.models import *


class UserProfile(User):
    nickname = models.OneToOneField(User, on_delete=models.CASCADE, related_name='nick')
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    followers = models.PositiveIntegerField()


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_follower')
    following = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_following')
    created_at = models.DateField(auto_now_add=True)


class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='post_user')
    image = models.ImageField(blank=True, null=True)
    caption = models.CharField(blank=True, null=True, max_length=500)
    created_at = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField('PostLike', related_name='post_likes')
    hashtag = models.CharField(blank=True, null=True, max_length=100)


class PostLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_post_like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_post_like')
    created_at = models.DateField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_comment')
    text = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(PostLike, related_name='comment')


class CommentLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comment_user')
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)


class Story(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='story_user')
    image = models.ImageField(blank=True, null=True)
    video = models.FileField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    expires_at = models.DateField()


class Group(models.Model):
    name = models.CharField(blank=True, null=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='group_creator')
    members = models.ManyToManyField(UserProfile, related_name='users')
    join_key = models.CharField(blank=True, null=True, max_length=100)



