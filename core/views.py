from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer, CategorySerializer, CommentSerializer

from core.models import Post, Category, Comment, Tag


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<slug:slug>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def cat_list(request):
	cat = Category.objects.all().order_by('-id')
	serializer = CategorySerializer(cat, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def post_list(request):
	posts = Post.objects.all().order_by('-id')
	serializer = PostSerializer(posts, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def post_detail(request, slug):
	posts = Post.objects.get(slug=slug)
	serializer = PostSerializer(posts, many=False)
	return Response(serializer.data)

@api_view(['GET'])
def comment_list(request, id):
	comment =	Comment.objects.filter(post_id=id)
	serializer = CommentSerializer(comment, many=False)
	return Response(serializer.data)