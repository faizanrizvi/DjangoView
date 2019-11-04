from django.conf.urls import url,include
from .views import  (post_list_view,
					login_required_view,
					post_detail_view,
					post_create_view,
					post_update_view,
					post_delete_view)


urlpatterns = [
    
    url(r'^$', post_list_view,name='post_list'),
    url(r'^create$', post_create_view,name='create'),
    url(r'^(?P<id>\d+)/edit/$', post_update_view, name='update'),
    url(r'^(?P<id>\d+)/$', post_detail_view,name='detail'),
    url(r'^(?P<id>\d+)/delete/$', post_delete_view,name='delete'),
    url(r'^public$', login_required_view,name='login_required')


    ]