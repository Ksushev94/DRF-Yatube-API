from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_id>/comments/',
         CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('posts/<int:post_id>/comments/<int:pk>/',
         CommentViewSet.as_view(
             {
                 'get': 'retrieve',
                 'put': 'update',
                 'patch': 'partial_update',
                 'delete': 'destroy'
             }
         )),
]
