from django.urls import path
from . import views

app_name = 'blog' #django2.0から必要になったnamespace定義
urlpatterns = [
    path('', views.post_list, name='post_list'),
	path('article/<int:pk>/', views.article, name='article'),	# 追加
]