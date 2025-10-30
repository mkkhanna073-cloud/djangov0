from  django.urls import path
from . import views

urlpatterns = [ 
    path('media/', views.media, name='media'),
    path('second/', views.second, name='second'),
    path('video/', views.video, name='video'),
    path('screen_1/', views.screen_1,name='screen_1'),
    path('screen_4/',views.screen_4,name='screen_4'),
]