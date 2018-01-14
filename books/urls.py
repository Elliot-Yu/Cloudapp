from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='Homepage'),
    url(r'^Login/$', views.login, name='login'),
    url(r'^showuser/$', views.show_user,name = 'show_user'),
    url(r'^regist/$', views.regist, name='regist'),
    #url(r'^index/$', views.index, name='index'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^create_new_group/$', views.create_new_group, name = 'createnewgroup'),
    url(r'^homepage/$', views.homepage, name = 'homepage'),
    url(r'^group/addme/$', views.group_addme, name='addme'),
    url(r'^group/quit_group/$', views.quit_group, name='quit'),
    url(r'^group/delete_group/$', views.delete_group, name='delete_group'),
    url(r'^group/complete_group/$', views.complete_group, name='complete_group'),
    url(r'^group_detail/(?P<id>[\d]+)$', views.group_detail,name = 'group_detail'),
    url(r'^groupList/$', views.grouplist,name ='groupList'),
    url(r'^comment/addo/$', views.comment_add_o,name ='comment_add_o'),
    url(r'^comment/add/$', views.comment_add,name ='comment_add'),
   # url(r'^my_group/(?P<username>[\w]+)$', views.my_group,name = 'my_group'),
    url(r'^my_group/$', views.my_group,name = 'my_group'),
    url(r'^myGroupDetail_organiser/(?P<id>[\w]+)$', views.group_detail_organiser,name='group_detail_organiser'),
    url(r'^myGroupDetail_member/(?P<id>[\w]+)$', views.group_detail_member,name='group_detail_member'),
    url(r'^regist/$', views.regist,name='regist'),
]