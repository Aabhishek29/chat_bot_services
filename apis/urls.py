# basic URL Configurations
from django.urls import include, path
# import routers
from rest_framework import routers
from . import views
# import everything from views
from .views import *

# define the router
router = routers.DefaultRouter()
#
# # define the router path and viewset to be used
router.register(r'chat-bot',views.GeeksViewSet )

# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    # path(r'chat-model', ChatModel, name="chat-model"),
    path('api-auth/', include('rest_framework.urls'))
]
