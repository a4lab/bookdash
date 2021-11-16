from django.urls import path
from . import views
app_name = 'images'

urlpatterns = [
    path('<int:id>/<slug:slug>', views.image_detail, name='detail'),
    path('create/', views.image_create, name='create'),
    path('like/', views.image_like, name='like'),
    # path('comment/', views.image_comment, name='comment'),
    path('', views.image_list, name='list'),
]