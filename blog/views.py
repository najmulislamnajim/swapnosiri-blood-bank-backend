from django.shortcuts import render
from rest_framework import viewsets
from .models import BlogModel,Comments
from .serializer import BlogSerializer,CommentsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    queryset=BlogModel.objects.all()
    serializer_class=BlogSerializer
    
class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class=CommentsSerializer
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("success")
        return Response(serializer.errors)
    
@api_view(['GET'])
def get_comments(request, blogId):
    try:
        comments = Comments.objects.filter(blog_id=blogId)
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)
    except Comments.DoesNotExist:
        return Response(status=404)
    
@api_view(['GET'])
def get_latest_blogs(request):
    try:
        # Retrieve the latest 8 blog posts ordered by created_date
        latest_blogs = BlogModel.objects.order_by('-created_date')[:8]
        serializer = BlogSerializer(latest_blogs, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
    
    
class LatestBlogs(viewsets.ModelViewSet):
    queryset=BlogModel.objects.order_by('-created_date')[:8]
    serializer_class=BlogSerializer