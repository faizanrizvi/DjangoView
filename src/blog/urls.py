from django.conf.urls import url,include
from .views import  post_list_view


urlpatterns = [
    
    url(r'^$', post_list_view,name='post_list')

    ]