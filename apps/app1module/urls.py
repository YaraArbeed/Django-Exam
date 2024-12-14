from django.urls import path, include
from apps.app1module import views

urlpatterns = [
 path('',views.index,name='index')

]
