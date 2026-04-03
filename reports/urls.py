from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('Add-newform/',views.addnew,name="addnew"),
    path('search/',views.search,name="search"),
    path('edit/<int:id>/', views.edit_record, name='edit'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('register/', views.register, name='register'),
    path('',views.rlogin,name='login'),
    
]