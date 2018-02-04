
from django.conf.urls import url
from . import views

#Anything that start or end with use post_list view

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
