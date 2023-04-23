from django.urls import path


from . import views

urlpatterns = [
    path('mama/', views.mamas),
    path('name/<str:name>', views.gen2, name='gen2')
]
