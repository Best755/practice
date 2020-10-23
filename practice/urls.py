from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve

from practice import views

app_name = "User"
urlpatterns = {
    path('upload/imag', views.imag, name="imag"),
}