from django.urls import path
from list import views as list_views

urlpatterns = [
    path('lists', list_views.index.as_view(), name='lists'),
    path('lists/<int:pk>', list_views.detailList.as_view()),
    path('lists/<int:pk>/mbtracks', list_views.listTracksByListPK.as_view()),
]