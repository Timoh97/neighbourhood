
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views




urlpatterns = [
path('',views.index, name='index'),
path("home/", views.home, name="home"),
path("profile/", views.profile, name="profile"),
path('create_profile/',views.create_profile,name = 'create_profile'),
path('create_post/',views.create_post,name = 'create_post'),
path('create_post/post/',views.post,name = 'post'),
path('update_profile/<int:id>',views.update_profile, name='update_profile'),
path("business/", views.business, name="business"),
path("post/", views.post, name="post"),
path('upload/project/', views.upload, name = "upload"),
path('accounts/profile/', views.index, name='accounts'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)