from django.urls import path,include
from .views import home_view, product_view, product_details, product_delete, export_file
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'movie', views.MovieView)
router.register(r'role', views.RoleView)
urlpatterns = [
    path('home/', home_view, name="home"),
    path('movie/', include(router.urls)),
    path('', product_view, name="product"),
    path('details/<int:id>', product_details, name="details"),
    path('download/<int:id>', export_file, name="download"),
    path('delete/<int:id>', product_delete, name="delete"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
            ]