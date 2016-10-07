from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^crystal/', include(crystal.urls)),
    url(r'^admin/', admin.site.urls),
]
