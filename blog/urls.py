from rest_framework.routers import DefaultRouter 
from django.urls import path,include
from .views import BlogViewSet,CommentsViewSet,get_comments,get_latest_blogs,LatestBlogs

router=DefaultRouter()
router.register('list',BlogViewSet)
router.register('latest',LatestBlogs)
router.register('comment',CommentsViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('list/<int:blogId>/comments',get_comments,name="get_comments"),
    path('latest-blogs/',get_latest_blogs,name="latest_blogs")
    
]