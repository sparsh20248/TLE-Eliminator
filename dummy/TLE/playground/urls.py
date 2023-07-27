from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_app),
    path('login/',views.login_page)
]
