from django.urls import path, include
#from .api import urls, views

from . import views

urlpatterns = [
    path('', views.chat_main, name='chat'),
    path('<int:pk>/', views.chat, name='chat_id'),
    path('api/', include('chat.api.urls')),
]
