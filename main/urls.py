from django.urls import path
from main import views

urlpatterns=[

    path('', views.index),
    path('projects/', views.projects),
    path('achievements/', views.achievements),
    path('education/', views.education),
    path('skills/', views.skills)
]
