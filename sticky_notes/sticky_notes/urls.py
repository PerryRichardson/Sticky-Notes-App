from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', include('notes.urls')),  # Sticky notes app
    path('posts/', include('posts.urls')),  # Testing app
]
