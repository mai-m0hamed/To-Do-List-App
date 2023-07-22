from django.urls import path
from .views import  loginPage,Tasklist,TaskDetail,TaskCreate,TaskUpdate,TaskDelete,Register
from django.contrib.auth.views import LogoutView


urlpatterns=[
    path('login/',loginPage.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register/',Register.as_view(),name='register'),
    path('',Tasklist.as_view(),name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('createtask/',TaskCreate.as_view(),name='createtask'),
    path('updatetask/<int:pk>/',TaskUpdate.as_view(),name='updatetask'),
    path('deletetask/<int:pk>/',TaskDelete.as_view(),name='deletetask'),





]