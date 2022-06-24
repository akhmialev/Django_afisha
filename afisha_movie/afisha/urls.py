from django.urls import path
from . import views

urlpatterns = [
    path('', views.MoviesView.as_view()),
    path('filter/', views.FilterMovieView.as_view(), name='filter'),
    path('search/', views.Search.as_view(), name='search'),
    path('add-rating/', views.AddStarRating.as_view(), name='add_rating'),
    path('<slug:slug>/', views.MovieDetailView.as_view(), name='afisha-detail'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review'),
    path('actor/<str:slug>/', views.ActorView.as_view(), name='actor_detail'),
]