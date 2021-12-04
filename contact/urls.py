from django.urls import include, path

from . import views

app_name='contact'

urlpatterns = [
    path('send-message',views.send_message , name='contact'),
]