from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name="account"

urlpatterns = [
    
    # path("",views.user_login,name="user_login"),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logged_out.html'), name='logout'),
    
    # password change
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='dash/password_change_form.html'),name='password_change'),
    path('password_change/done',auth_views.PasswordChangeDoneView.as_view(),name='auth/password_change_done.html'),
    
    # reset pass 
    
    path('users/', views.user_list, name='user_list'),
    path('users/<username>/', views.user_detail, name='user_detail'),

    path('register/', views.register, name='register'),
    

    path('edit/', views.edit, name='edit'),
    path('', views.dashboard, name='dashboard'),
    
]




# Django also provides the authentication URL patterns that you just created. You 
# can comment out the authentication URL patterns that you added to the urls.py 
# file of the account application and include django.contrib.auth.urls instead, 
# as follows:
# from django.urls import path, include
# # ...
# urlpatterns = [
#     # ...
#     path('', include('django.contrib.auth.urls')),
# ]