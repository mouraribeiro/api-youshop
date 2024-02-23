from django.contrib import admin

from django.urls import include, path
from rest_framework import routers


from appys.views import *
from rest_framework.authtoken import views


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'userProfile', UserProfileViewSet, basename='user profile')
router.register(r'accounts', AccountViewSet, basename='account')
router.register(r'trees', TreeViewSet, basename='tree')
router.register(r'plants', PlantViewSet, basename='plant')
router.register(r'location', LocationViewSet, basename='location')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
