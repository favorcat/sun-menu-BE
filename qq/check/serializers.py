from rest_framework import serializers
from .models import Checklist, Board, Reviewlist, Restaurant, Menu

class CheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist
        fields = ['pk', 'user', 'content', 'place', 'stufflist']

class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist
        fields = ['pk', 'user', 
                  'taste', 'quality', 'cost', 'clean', 'quantity', 'menu_name', 'cafeteria_name', 'created_at', 'updated_at']
        #model = '__all__'


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['pk', 'user', 'title', 'content', 'created_at', 'updated_at']
        #model = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewlist
        fields = ['pk', 'avg_taste', 'avg_cost', 'avg_clean', 'avg_quality', 'avg_quantity', 'menu_name', 'cafeteria_name',]

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['pk', 'eng_name', 'kor_name', 'location', 'phone', 'operating_day','operating_time', 'notice_contents', 'notice_registered', 'lat', 'lng']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['pk', 'menu_name', 'cafeteria', 'price', 'type']
