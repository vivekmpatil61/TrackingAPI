from django.urls import path
from .views import generate_tracking_number, tracking_form
# from .views import tracking_form

urlpatterns = [
    path('generate-tracking-number/', generate_tracking_number, name='generate-tracking-number'),
    path('tracking-form/', tracking_form, name='tracking_form'),


]
# urlpatterns = [

#     path('tracking-form/', tracking_form, name='tracking_form'),

# ]