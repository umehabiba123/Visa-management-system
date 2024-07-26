from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path("form_display/<str:passport_number>/",views.form_display, name="form_display")
    # path("term/", views.term_and_conditions, name="term_and_conditions")
]