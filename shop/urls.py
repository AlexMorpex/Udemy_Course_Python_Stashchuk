from django.urls import path
from . import views
# Здесь мы связываем функцию вида с маршрутом

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>', views.single_course, name='single_course'),
]
