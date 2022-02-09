from django.contrib import admin
from django.urls import path

from .main import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='list'),
    path('create/', views.ProjectCreateView.as_view(), name='create'),
    path('admin/', admin.site.urls),
]
