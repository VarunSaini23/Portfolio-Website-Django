from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('detail/<int:blog_id>',views.blogdetail,name='blogdetail')
]
