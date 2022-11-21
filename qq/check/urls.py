from django.urls import path
from . import views

app_name = 'checks'

urlpatterns = [
    #path('', views.check_list),
    path('create/', views.create_check),
    path('create/<str:name>/<str:menu>', views.get_review),
    path('announce/', views.create_board),
    path('announce/<int:pk>', views.get_board),
    
    path('cafe/', views.create_restaurant),  #가게 생성
    path('cafe/<str:eng_name>', views.get_cafeinfo),  # 카페 정보 불러오는 api

    path('menu/', views.create_menu),  #메뉴 생성
    path('menu/<str:eng_name>', views.get_cafemenu),  # 가게에서 파는 메뉴 불러오는 api 
    path('menu/<str:eng_name>/<str:menu>', views.get_menuinfo),  # 메뉴 정보 불러오는 api 

]
