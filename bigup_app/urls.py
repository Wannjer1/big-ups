from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('',views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    # registration paths
    path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='registration/logout.html'), name="logout"),
    
    # api paths
    path('bigapi/', views.bigapi, name='bigapi'),
    path('bigapi/api/profile/', views.ProfileList.as_view(), name='api-profile'),
    path('bigapi/api/project/', views.ProjectList.as_view(), name='api-project'),
   
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)