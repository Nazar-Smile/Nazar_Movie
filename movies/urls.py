from django.urls import path

from . import views

urlpatterns = [
    path("", views.MoviesView.as_view()),
    path("add-rating", views.FilterMoviesView.as_view(), name='json_filter'),
    path("json-filter/", views.AddStarRating.as_view(), name='add_rating'),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("actor/<str:slug>/", views.ActorView.as_view(), name="actor_detail"),
    path("category/list/<int:pk>/", views.CategoryListView.as_view(), name="category_list"),
]