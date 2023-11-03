from django.urls import path
from .views import sing_in, sing_up, forget_pass, sing_out, success, fail

urlpatterns = [
    path('singin/', sing_in, name="singin"),
    path('singup/', sing_up, name="singup"),
    path('sing_out/', sing_out, name="sing_out"),
    path('forget_pass/', forget_pass, name="forget_pass"),
    path('success/', success, name="success"),
    path('fail/', fail, name="fail"),
]
