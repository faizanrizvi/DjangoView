from django.conf.urls import url,include
from .views import  post_list_view,login_required_view,post_detail_view


urlpatterns = [
    
    url(r'^$', post_list_view,name='post_list'),
    url(r'^(?P<id>\d+)/$', post_detail_view,name='detail'),
    url(r'^public$', login_required_view,name='login_required')


    ]