from django.urls import path
from .views import UserList, UserDetail # new
urlpatterns = [
path("users/", UserList.as_view()), # new
path("users/<int:pk>/", UserDetail.as_view()), # new

]