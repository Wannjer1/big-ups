from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('',views.home, name='home'),
    # registration paths
    path('signup/', views.signup, name='signup'),
    # api paths
    path('api/profile/', views.ProfileList.as_view(), name='api-profile'),
    path('api/project/', views.ProjectList.as_view(), name='api-project'),
   
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)