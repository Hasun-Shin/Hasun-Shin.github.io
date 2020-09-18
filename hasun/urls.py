from django.contrib import admin
from django.urls import path
from shin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('https://hasun-shin.github.io/', views.main),
]
