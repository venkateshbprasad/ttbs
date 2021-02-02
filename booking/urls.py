from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name= 'dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.logIn, name='login'),
    path('logout/', views.logOut, name='logout'),
    path('book/<str:pk>/', views.book, name='book'),
    path('createtrain/', views.createTrain, name='createtrain'),
    path('accountsettings/', views.accountsettings, name='accountsettings'),
    path('history/', views.history, name='history'),

]
