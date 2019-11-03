from django.conf.urls import url,include
from .views import  post_list_view,login_required_view


urlpatterns = [
    
    url(r'^$', post_list_view,name='post_list'),
    url(r'^public$', login_required_view,name='login_required')


    ]