from factorial_api import views
from django.urls import path


urlpatterns = [
    path("", views.factorial)
]