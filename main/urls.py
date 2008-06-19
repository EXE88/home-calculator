from django.urls import path, include
from . import views

urlpatterns = [
    path('project/create/', views.CreateNewProject.as_view(), name='create-new-project'),
    path('project/full/<int:pk>/',views.ProjectFullDetails.as_view(),name='project-full-details'),
    path('project/review/<int:pk>/', views.ProjectReview.as_view(), name='project-review'),
]