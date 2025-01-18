from django.contrib import admin  
from django.urls import path       
from authentication.views import *  
from django.conf import settings   
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  
from django.conf.urls.static import static
from authentication.views import *

urlpatterns = [
    path('',home, name='home'),
    path('home/', home, name="recipes"),      
    path("admin/", admin.site.urls),          
    path('login/', login_page, name='login_page'),    
    path('register/', register_page, name='register'),  
    path('logout/', logout_view, name='logout_view'),
    path('password-reset/', password_reset_request, name='password_reset'),
    path('password-reset/done/', password_reset_done, name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),
    path('password-reset-complete/', password_reset_complete, name='password_reset_complete'),
]

# Serve media files if DEBUG is True (development mode)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()