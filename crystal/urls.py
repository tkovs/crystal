from django.conf.urls import url
from .                import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^ranking/$', views.ranking, name='ranking'),
	url(r'^provas/$', views.test_list, name='test_list'),
	url(r'^prova/(?P<id>\d+)/$', views.test_details, name='test_details')
]