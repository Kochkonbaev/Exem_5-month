from django.urls import path
from .views import *
 

urlpatterns = [
    path('', all_posts, name='all_posts'),
    path('new/', new_post, name='new_post'),
    path('<int:pk>/', post_detail, name='post_detail'),
    path('<int:pk>/edit/', post_edit, name='post_edit'),
    path('<int:pk>/delete/', post_delete, name='post_delete'),

]