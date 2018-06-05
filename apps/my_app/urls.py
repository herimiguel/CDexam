from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
	url(r'^login$', views.login),
    # url(r'^success$', views.success, name='success'),
    url(r'^logOut$', views.logOut, name='logOut'),
	url(r'^toItems/(?P<id>\d+)$', views.toItems, name='toItems'),
    url(r'^addItem$', views.addItem, name='addItems'),
	url(r'^viewItems$', views.viewItems, name='viewItems'),
	url(r'^addToMyItem/(?P<item_id>\d+)$', views.addToMyItem, name='addToMyItem'),
	url(r'^deleteItem/(?P<item_id>\d+)$', views.deleteItem, name='deleteItem'),
	url(r'^deleteFromD/(?P<id>\d+)$', views.deleteFromD, name='deleteFromD'),
]