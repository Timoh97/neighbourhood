
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


app_name = 'application'

urlpatterns = [
path('',views.index, name='index'),
path("home/", views.home, name="home"),
path("profile/", views.profile, name="profile"),
path("business/", views.business, name="business"),
path("post/", views.post, name="post"),
path('accounts/profile/', views.index, name='accounts'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)