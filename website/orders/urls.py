
from django.contrib import admin
from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'orders'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),

    url(r'^orderInfo/$', views.OrderList),

    url(r'^orderInfo/(?P<pk>[0-9]+)/$', views.OrderDetail),

    url(r'admin/', admin.site.urls),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    #album_id
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = "detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)