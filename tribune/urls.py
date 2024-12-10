from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    path(r'accounts/', include('django_registration.backends.activation.urls')),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),    
]
