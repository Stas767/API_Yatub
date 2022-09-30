from django.shortcuts import get_object_or_404

from rest_framework import mixins, viewsets
from rest_framework import permissions
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Group, Post
from api.permission import AuthorOrReadOnly
from api.serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer
)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        post = get_object_or_404(
            Post,
            pk=self.kwargs.get("post_id")
        )
        new_queryset = post.comments
        return new_queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = Post.objects.get(pk=post_id)
        serializer.save(
            author=self.request.user,
            post=post
        )


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (AuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        followers = self.request.user.follower.all()
        return followers

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )
