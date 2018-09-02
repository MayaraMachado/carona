from . import views
from django.urls import path


urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='registrar'),    
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout_View, name='logout'),
]