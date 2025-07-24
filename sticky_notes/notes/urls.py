from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('<int:pk>/', views.note_detail, name='note_detail'),
    path('add/', views.note_create, name='note_create'),  # ✅ correct name
    path('<int:pk>/edit/', views.note_update, name='note_update'),
    path('<int:pk>/delete/', views.note_delete, name='note_delete'),
]
