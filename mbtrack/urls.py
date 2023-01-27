from django.urls import path
from mbtrack import views

urlpatterns = [
    path('mbtracks', views.index.as_view(), name='mbtracks'),
]
