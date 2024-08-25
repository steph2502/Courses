from django.urls import path,include
from . import views

urlpatterns = [
    path('list/', views.course_list),
    path('detail/<int:id>',views.course_detail),
    
]