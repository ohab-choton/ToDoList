from django.urls import path 
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.loginPage,name='login'),
    
    path('update/<str:name>/',views.updateTask,name='update'),
    path('delete/<str:name>/',views.deleteTask,name='delete'),
    path('logout/', views.logoutPage, name='logout'),
       
]
