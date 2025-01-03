from django.urls import path
from . import views
urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_create, name='student_create'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.course_create, name='course_create'),
    path('courses/edit/<int:pk>/', views.course_edit, name='course_edit'),
    path('courses/<int:pk>/delete/', views.course_delete, name='course_delete'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/mark/', views.attendance_mark, name='attendance_mark'),
]