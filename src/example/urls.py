from django.conf.urls import url
from .views import orders_list, edit_order


urlpatterns = [
    url(r'^$', orders_list, name='orders_list'),
    url(r'create$', edit_order, name='create_order'),
    url(r'edit/(?P<pk>[0-9]*)/$', edit_order, name='edit_order'),
]
