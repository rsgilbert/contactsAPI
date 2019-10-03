from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from contacts import views as contact_views
# import contacts
from rest_framework.authtoken import views


# routers to determine the url conf
router = routers.DefaultRouter()
router.register(r'contacts', contact_views.ContactViewSet)
router.register(r'finance', contact_views.FinanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('auth/token', views.obtain_auth_token),
    path('', include('contacts.urls')),

]
