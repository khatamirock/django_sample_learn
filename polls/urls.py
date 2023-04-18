from django.urls import path


from . import views

urlpatterns = [
    path('mama/', views.mamas),
]
