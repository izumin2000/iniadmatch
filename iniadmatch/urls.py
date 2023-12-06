from django.urls import path, include
from iniadmatch import views


urlpatterns = [
    path("", views.TopView.as_view(), name='top'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('auth/', include('social_django.urls', namespace='social')),  
]