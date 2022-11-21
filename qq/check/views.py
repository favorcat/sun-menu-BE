from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CheckListSerializer, CheckSerializer, BoardSerializer, ReviewSerializer, RestaurantSerializer, MenuSerializer
from .models import Checklist, Board, Restaurant, Menu
from rest_framework import status
from rest_framework.parsers import JSONParser

# 글 게시 (리뷰)
@api_view(['POST'])
def create_check(request):
    serializer = CheckSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

# 리뷰 가져오기
from django.core import serializers
from django.http import HttpResponse

from django.db.models import Avg
from .models import Reviewlist
from .serializers import ReviewSerializer
@api_view(['GET'])
def get_review(request, name, menu):
  try:
    post = Checklist.objects.filter(cafeteria_name=name,menu_name=menu)
    print(post)
    
  except Board.DoesNotExist: 
    return Response(status = status.HTTP_404_NOT_FOUND)
  
  if request.method =="GET":
    post = Checklist.objects.filter(cafeteria_name=name,menu_name=menu)
    avg_cost = post.aggregate(Avg('cost'))
    avg_taste = post.aggregate(Avg('taste'))
    avg_clean = post.aggregate(Avg('clean'))
    avg_quality = post.aggregate(Avg('quality'))
    avg_quantity = post.aggregate(Avg('quantity'))

    avg_cost = avg_cost['cost__avg']
    avg_taste = avg_taste['taste__avg']
    avg_clean = avg_clean['clean__avg']
    avg_quality = avg_quality['quality__avg']
    avg_quantity = avg_quantity['quantity__avg']

  
    p = Reviewlist.objects.create(menu_name = menu, cafeteria_name = name,
                              avg_cost = avg_cost,
                              avg_taste = avg_taste,
                              avg_clean = avg_clean,
                              avg_quality = avg_quality,
                              avg_quantity = avg_quantity,
                              )
    ppk =p.pk
    queryset = Reviewlist.objects.get(pk=ppk)
    serializer_class = ReviewSerializer(queryset)

    return Response(serializer_class.data)
    
    
# 글 게시 (가게주인)
from django.contrib.admin.views.decorators import staff_member_required

@api_view(['POST', 'GET'])
def create_board(request):
  if request.method == 'GET':
    post = Board.objects.all()
    serializer = BoardSerializer(post, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = BoardSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      l = request.user.groups.values_list('name',flat = True) # QuerySet Object
      group = list(l)
      print(group)
      return Response(serializer.data, status=status.HTTP_201_CREATED)

  return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


from django.contrib.admin.views.decorators import staff_member_required
from .decorators import check_owner
from django.views.decorators.csrf import csrf_protect 

#@csrf_protect 
#@check_owner
@api_view(['GET', 'PUT', 'DELETE'])
def get_board(request, pk):
  try:
    post = Board.objects.get(pk=pk)
  except Board.DoesNotExist:
    return Response(status = status.HTTP_404_NOT_FOUND)
  
  if request.method =="GET":
    serializer = BoardSerializer(post)
    return Response(serializer.data)
  
  elif request.method == 'PUT':
    #data = JSONParser().parse(request)
    serializer = BoardSerializer(post, data=request.data)

    if serializer.is_valid():
      serializer.save()
    
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


##################################################################################
## 카페

@api_view(['POST', 'GET'])
def create_restaurant(request):
  if request.method == 'GET':
    post = Restaurant.objects.all()
    serializer = RestaurantSerializer(post, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = RestaurantSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_cafeinfo(request, eng_name):
  try:
    post = Restaurant.objects.get(eng_name=eng_name)
  except Restaurant.DoesNotExist:
    return Response(status = status.HTTP_404_NOT_FOUND)
  
  if request.method =="GET":
    serializer = RestaurantSerializer(post)
    return Response(serializer.data)

##########################################################################
#   메뉴

@api_view(['POST', 'GET'])
def create_menu(request):
  if request.method == 'GET':
    post = Menu.objects.all()
    serializer = MenuSerializer(post, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = MenuSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_cafemenu(request, eng_name):
  try:
    post = Menu.objects.get(cafeteria=eng_name)
  except Menu.DoesNotExist:
    return Response(status = status.HTTP_404_NOT_FOUND)
  
  if request.method =="GET":
    serializer = MenuSerializer(post, many=True)
    return Response(serializer.data)
  

@api_view(['GET'])
def get_menuinfo(request, eng_name, menu):
  try:
    post = Menu.objects.get(cafeteria=eng_name, menu_name= menu)
  except Menu.DoesNotExist:
    return Response(status = status.HTTP_404_NOT_FOUND)
  
  if request.method =="GET":
    serializer = MenuSerializer(post)
    return Response(serializer.data)
  
