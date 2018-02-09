
from django.contrib import admin
from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'music'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),

    url(r'albumInfo/', views.AlbumList.as_view()),

    url(r'admin/', admin.site.urls),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    #album_id
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = "detail"),
    #/music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    #/music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    #/music/album/2/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.ALbumDelete.as_view(), name='album-delete'),
]

urlpatterns = format_suffix_patterns(urlpatterns)