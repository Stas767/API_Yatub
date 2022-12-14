from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='add_comments'
)
router.register(r'groups', GroupViewSet)
router.register(r'follow', FollowViewSet, basename='following')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls.jwt')),
]
