from django.urls import path

from . import views

urlpatterns = [
    path("", views.MoviesView.as_view(), name='index'), # Главная страница
    path("detail/<int:pk>/", views.MovieDetailView.as_view(), name='movie_detail'),  # Детальная страница с Фильмами
    path("actor/<str:slug>/", views.ActorView.as_view(), name="actor_detail"),  # Детальная страница Актера
    path("films/", views.FilmsView.as_view(), name='films'), # Страница с Фильмами
    path("anime/", views.AnimeView.as_view(), name='anime'), # Страница с Аниме
    path("serials/", views.SerialsView.as_view(), name='serials'), # Страница с Сериалами
    path("detail/comment/create/<int:post_id>/", views.CommentCreateView.as_view(), name="create_comment"), # Комментарии/Отзывы
    path("catalog/list/", views.CatalogListView.as_view(), name='catalog'), # Страница со всеми категориями
    path('catalog/list/new/', views.catalog_list, name='catalog_list'),  # Страница поиска всех категорий
    path('serials/list/new/', views.serials_list, name='serials_list'), # Страница поиска Сериалов
    path('films/list/new/', views.films_list, name='films_list'), # Страница поиска Фильмов
    path('anime/list/new/', views.anime_list, name='anime_list'), # Страница поиска Аниме
    path("search/", views.Search.as_view(), name='search'), # Страница поиска
    path('about/', views.about, name='about'),  # О сайте




]
