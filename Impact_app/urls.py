from django.contrib import admin
from django.urls import path
from Impact_app import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('register/', views.register,name='register'),
    path('login/', views.login, name='login'),
    path('adminhome/',views.adminhome,name='adminhome')

]

