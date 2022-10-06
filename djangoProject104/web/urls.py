from django.urls import path

from djangoProject104.web.views import index

urlpatterns = (
    path('', index, name='index'),
)
