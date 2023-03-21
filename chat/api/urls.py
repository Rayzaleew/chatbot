from django.urls import path, include
from . import views

urlpatterns = [
    path('messages/<int:pk>', views.getMessages),
    path('get_prompt_result/', views.get_prompt_result),
]