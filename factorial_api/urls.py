from factorial_api import views
from django.urls import path


urlpatterns = [
    path("factorial/", views.factorial),
    path("", views.index)
]