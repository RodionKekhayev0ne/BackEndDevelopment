from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # path('update/', views),
    # path('movies/<str:id>/', views),
    path('createAction/', views.createAction),
    path('createAction/create/', views.create),
    path('updateAction/<str:pk>', views.updateAction, name='update-action'),
    path('updateAction/update/<str:pk>', views.update, name='update'),
    path('', views.main),
    path('done/<str:pk>', views.done),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
