from django.urls import path
from.import views

urlpatterns = [
    path('fv/',views.first_view),
    path('sv/',views.second_view),
    path('tv/', views.third_view)

]
