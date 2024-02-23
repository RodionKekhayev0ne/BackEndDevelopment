from django.urls import path
from . import views


urlpatterns = [
    # path('update/', views),
    # path('movies/<str:id>/', views),
    path('createAction/', views.createAction),
    path('createAction/create/', views.create),
    path('updateAction/', views.updateAction),
    path('updateAction/update/<str:id>/', views.update),
    path('', views.main),
]