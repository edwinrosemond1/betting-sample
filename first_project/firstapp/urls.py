from django.conf.urls import url
from django.urls import path, re_path
from firstapp import views


app_name = 'firstapp'

urlpatterns = [
    path(r'^users/$', views.users, name ='users'),
    path('firstapp/', views.register, name = 'register'),
    re_path(r'^$', views.register, name ='register'),
    re_path(r'^relative/$', views.relative, name = 'relative'),
    re_path(r'^register/$', views.register, name ='register'),
    re_path(r'^user_login/$', views.user_login, name = 'user_login'),
    #re_path(r'^formpage/$', views.form_name_view, name = 'formpage')
]

#template tagging
