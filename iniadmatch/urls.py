from django.urls import path, include
from iniadmatch import views


urlpatterns = [
    path("", views.TopView.as_view(), name="top"),
    path("schedule/<int:pk>", views.ScheduleView.as_view(), name="schedule"),
    path("search", views.SearchView.as_view(), name="search"),
    path("setting", views.SettingView.as_view(), name="setting"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("auth/", include("social_django.urls", namespace="social")),  
]