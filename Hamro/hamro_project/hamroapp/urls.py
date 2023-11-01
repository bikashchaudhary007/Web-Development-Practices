from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
     path('', views.landing_page, name='landing_page'),
    path('login/', views.login_view, name='login'),
    
]
