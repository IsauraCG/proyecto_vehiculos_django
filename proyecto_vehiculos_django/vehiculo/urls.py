from django.urls import path
from .views import IndexPageView, home_page_not_login

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),  # registrando ruta,
    path('home/', home_page_not_login, name='home')  # registrando ruta para usuario not login
]