from django.urls import path
from . import views
from django.conf.urls import include, url

app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.Indexview.as_view(), name='index'),
    # default homepage created as ''are left blank


    path('register/', views.UserFormView.as_view(), name='register'),

    # /music/712/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # /music/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/2/
    path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/2/delete/
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),
]
