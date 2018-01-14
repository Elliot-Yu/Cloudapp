from django.conf.urls import url, include
from django.contrib import admin
admin.autodiscover()

from mysite import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.regist),
    url(r'^books/', include('books.urls')),
    url(r'^Homepage/$', views.Homepage),
    #('^grouplist/$', views.grouplist),
]