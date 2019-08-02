from django.urls import path
from auth.views import CreateUser

urlpatterns = [
    path('create', CreateUser.as_view())
]
