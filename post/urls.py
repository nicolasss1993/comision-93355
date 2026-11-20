from post.views import *
from django.urls import path


urlpatterns = [
    path("", home, name="principal"),
]
