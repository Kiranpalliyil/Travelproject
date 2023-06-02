from.import views
from django.urls import path

# from travelproject.travelapp import views

urlpatterns = [
    path('',views.demo,name='demo'),
    # path('find/',views.find,name='find'),
    # path('sub/',views.subtraction,name='subtraction')
    # path('div/',views.division,name='division')



]
