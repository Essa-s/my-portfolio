from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path("", views.home, name="app"),
    path('basic=info-view/', views.BasicInfoListView.as_view(), name='basic-info-view'),
    path('basic-info-create/', views.BasicInfoCreateView.as_view(), name='basic-info-create'),
]