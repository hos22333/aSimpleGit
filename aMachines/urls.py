from django.urls import path
from . import views


urlpatterns = [
    path('page1/', views.page1_view, name='page1'),
    path('page2/', views.page2_view, name='page2'),
    path('page3/', views.page3_view, name='page3'),
    path('page4/', views.page4_view, name='page4'),
    path('page5/', views.page5_view, name='page5'),
    path('page6/', views.page6_view, name='page6'),
    path('page7/', views.page7_view, name='page7'),
    path('page8/', views.page8_view, name='page8'),
    path('page9/', views.page9_view, name='page9'),
    path('page10/', views.page10_view, name='page10'),
    path('page11/', views.page11_view, name='page11'),
    path('page12/', views.page12_view, name='page12'),
    path('page13/', views.page13_view, name='page13'),
    path('page14/', views.page14_view, name='page14'),
    path('page15/', views.page15_view, name='page15'),
    path('authorization/', views.authorization_view, name='authorization'),
    path('logs/', views.view_logs, name='view_logs'),
]