from django.conf.urls import url
import views
app_name='music'
urlpatterns = \
    [url(r'^$', views.IndexView.as_view(), name='index') , #/music/
     url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name="detail"),#/music/712/'/
     url(r'^album/add',views.CreateAlbum.as_view(),name="add-album"),
     url(r'^album/(?P<pk>[0-9]+)/delete$', views.DeleteAlbum.as_view(), name="delete-album"),
     url(r'^album/(?P<pk>[0-9]+)/update$', views.UpdateAlbum.as_view(), name="update-album"),
     url(r'^album/(?P<pk>[0-9]+)/add_song$',views.CreateSong.as_view(),name="add-song"),
     url(r'^album/(?P<pk>[0-9]+)/delete_song$',views.DeleteSong.as_view(),name="delete-song"),
     url(r'^all_songs$',views.all_songs,name="all-songs")
     ]