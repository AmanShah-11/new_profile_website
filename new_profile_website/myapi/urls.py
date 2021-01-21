from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectView)

urlpatterns = [
    path('random', views.random, name="random"),
    path('', include(router.urls)),
]