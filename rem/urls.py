from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url('add', views.addRem,name='add'),
    url('details/(?P<id>\w{0,50})/$' , views.details ),
    url('complete/(?P<id>\w{0,50})/$' , views.completeRem , name='complete')
]
