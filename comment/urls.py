from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, post_detail, postView, addPost,submit_form


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
# router.register(r)

# api/postd/2 or api/postview
urlpatterns = [
    path('', include(router.urls)),
    path('postd/<int:id>', post_detail),
    path('postview/', postView),
    path('addpost/', addPost),
    path('submit_form/',submit_form),
     

]
