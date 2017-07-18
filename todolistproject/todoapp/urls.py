from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^init$', views.get_init_data, name='init'),
    url(r'^post$', views.add_new, name="post"),
    url(r'^delete$', views.delete_object, name="delete"),
]
