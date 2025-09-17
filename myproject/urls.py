from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from aUsers import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.login_view, name='home'),  # Redirect to login as home
    path('register/', user_views.register_view, name='register'),
    path('login/', user_views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='aUsers/logout.html'), name='logout'),
    path('profile/', user_views.profile_view, name='profile'),
    path('change-username/', user_views.change_username, name='change_username'),
    path('change-password/', user_views.change_password, name='change_password'),
    path('machines/', include('aMachines.urls')),
]