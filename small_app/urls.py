
# from django.conf.urls import url
# from django.urls import include, re_path
from django.urls import path
from .views import TaskList ,TaskDetail ,TaskCreate ,TaskUpdate ,TaskDelete ,CustomLoginView , RegisterPage
from django.contrib.auth.views import LogoutView
app_name  = 'small_app'

urlpatterns = [
    path('', TaskList.as_view() , name='tasks'),
    path('<int:pk>/', TaskDetail.as_view() , name='task'),
    path('task-create', TaskCreate.as_view() , name='create'),
    path('update/<int:pk>/', TaskUpdate.as_view() , name='update'),
    path('delete/<int:pk>/', TaskDelete.as_view() , name='delete'),
    path('login', CustomLoginView.as_view() , name='login'),
    path('logout', LogoutView.as_view(next_page='calcs:login') , name='logout'),
    path('register', RegisterPage.as_view() , name='register'),
]
