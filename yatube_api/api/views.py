from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from .permissions import AuthorOrReadOnly, ReadOnly
from posts.models import Comment, Follow, Group, Post, User
from .serializers import (CommentSerializer, FollowSerializers,
                          PostSerializer, GroupSerializer)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        new_queryset = get_object_or_404(Post, pk=post_id).comments.all()
        return new_queryset


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializers
    permission_classes = permissions.IsAuthenticated
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        new_queryset = get_object_or_404(User, pk=user_id).follow.all()
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
