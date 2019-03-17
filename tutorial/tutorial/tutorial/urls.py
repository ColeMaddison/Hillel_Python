# from sys import path as sys_path
# from os import path as os_path
# sys_path.append(os_path.abspath(os_path.join('..', '..')))
import sys
sys.path.append('/home/dk/hillel-py/hillel_python/tutorial')

from django.urls import include, path
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]