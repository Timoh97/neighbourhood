
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views



urlpatterns = [
path('',views.index, name='index'),
path('home/',views.home, name='home'),
path('accounts/profile/', views.index, name='index'),
path("profile/", views.profile, name="profile"), # profile page
path("profile/update/", views.update_profile, name="update_profile"), # profile update page
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)