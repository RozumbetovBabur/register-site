from django.urls import path
from .views import *

urlpatterns = [
    path('',index_page,name="main"),
    path('get_user/',get_user_name,name="user_table"),
    path('get_user/<int:user_id>/',delete_user,name="delete_user"),
]