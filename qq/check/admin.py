from django.contrib import admin

# Register your models here.
from .models import Board, Checklist, Restaurant, Menu

# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'content', 'created_at', 'updated_at')

class ChecklistdAdmin(admin.ModelAdmin):
    list_display = ('user', 'menu_name', 'cafeteria_name', 'taste', 'quality', 'cost', 'clean', 'quantity','created_at')

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('eng_name', 'kor_name', 'location', 'phone', 'operating_day','operating_time', 'notice_contents', 'notice_registered', 'lat', 'lng')

class MenuAdmin(admin.ModelAdmin):
    list_display = ('menu_name', 'cafeteria', 'price', 'type')

admin.site.register(Board, BoardAdmin)
admin.site.register(Checklist, ChecklistdAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Menu, MenuAdmin)