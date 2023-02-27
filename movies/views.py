from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.base import View

from .forms import CommentCreateForm
from .models import Movie, Actor, Genre, Comment

from django.db.models import Q


class GenreYear:
    """Жанры и года выхода фильмов"""
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values("year")


class MoviesView(GenreYear, ListView):
    """Список всех категорий на главной странице"""
    model = Movie
    # queryset = Movie.objects.filter(draft=False)
    queryset = Movie.objects.filter(draft=False).order_by('-id')

    paginate_by = 8
    template_name = "movies/movie_list.html"


class FilmsView(GenreYear, ListView):
    """Список всех фильмов"""
    model = Movie
    # queryset = Movie.objects.filter(draft=False)
    queryset = Movie.objects.filter(category="1", draft=False).order_by('-id')
    paginate_by = 4
    template_name = "movies/films.html"


class AnimeView(GenreYear, ListView):
    """Список всех аниме"""
    model = Movie
    queryset = Movie.objects.filter(category="2", draft=False).order_by('-id')
    paginate_by = 4
    template_name = "movies/anime.html"


class SerialsView(GenreYear, ListView):
    """Список всех сериалов"""
    model = Movie
    queryset = Movie.objects.filter(category="3", draft=False).order_by('-id')

    paginate_by = 4
    template_name = "movies/serials.html"


class CatalogListView(ListView):
    """Список всех категорий на страничке ВСЕ КАТЕГОРИИ"""
    template_name = "movies/catalog.html"
    model = Movie
    paginate_by = 4
    queryset = Movie.objects.filter(draft=False).order_by('-id')
    # queryset = Movie.objects.filter(draft=False)


class MovieDetailView(GenreYear, DetailView):
    """Детальная страница фильма с описанием"""
    template_name = "movies/movie_detail.html"
    model = Movie
    # slug_field = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentCreateForm()
        return context


class ActorView(Genre, DetailView):
    """Вывод информации о актере"""
    model = Actor
    movie = Movie.objects.filter(draft=False).order_by('-id')
    template_name = "movies/actor.html"
    slug_field = "name"
    queryset = Actor.objects.order_by('-id')


class FilterMoviesView(GenreYear, ListView):
    """Фильтрация всех категорий"""
    # template_name = "movies/catalog.html"
    # paginate_by = 1

    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        ).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["year"] = ''.join([f"year={x}&" for x in self.request.GET.getlist("year")])
        context["genre"] = ''.join([f"genre={x}&" for x in self.request.GET.getlist("genre")])
        return context


class Search(ListView):
    """Поиск фильмов"""
    # template_name = 'index.html'
    # context_object_name = 'films'
    # paginate_by = 1

    def get_queryset(self):
        return Movie.objects.filter(title__icontains=self.request.GET.get("q")).distinct()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context


class CommentCreateView(LoginRequiredMixin, FormView):
    """Комментарии/Отзывы"""
    form_class = CommentCreateForm
    model = Comment

    def form_valid(self, form):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Movie, id=post_id)
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.post = post
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("movie_detail", kwargs={"pk":self.kwargs.get("post_id")})


def catalog_list(request):
    """Страница поиска всех категорий"""
    genre = request.GET.get('genre')
    year = request.GET.get('year')

    # Инициализация queryset'а
    movies = Movie.objects.all()

    # Фильтрация по жанру
    if genre:
        movies = movies.filter(genres__name=genre).order_by('-id')

    # Фильтрация по году
    if year:
        movies = movies.filter(year=year).order_by('-id')

    context = {
        'movies': movies
    }

    return render(request, 'movies/catalog.html', context)


def anime_list(request):
    """Страница поиска всех аниме"""
    genre = request.GET.get('genre')
    year = request.GET.get('year')

    # Инициализация queryset'а
    movies = Movie.objects.all()

    # Фильтрация по жанру
    if genre:
        movies = movies.filter(genres__name=genre, category="2").order_by('-id')

    # Фильтрация по году
    if year:
        movies = movies.filter(year=year, category="2").order_by('-id')

    context = {
        'movies': movies
    }

    return render(request, 'movies/anime.html', context)


def films_list(request):
    """Страница поиска всех фильмов"""
    genre = request.GET.get('genre')
    year = request.GET.get('year')

    # Инициализация queryset'а
    movies = Movie.objects.all()

    # Фильтрация по жанру
    if genre:
        movies = movies.filter(genres__name=genre, category="1").order_by('-id')

    # Фильтрация по году
    if year:
        movies = movies.filter(year=year, category="1").order_by('-id')

    context = {
        'movies': movies
    }

    return render(request, 'movies/films.html', context)


def serials_list(request):
    """Страница поиска всех скриалов"""
    genre = request.GET.get('genre')
    year = request.GET.get('year')

    # Инициализация queryset'а
    movies = Movie.objects.all()

    # Фильтрация по жанру
    if genre:
        movies = movies.filter(genres__name=genre, category="3").order_by('-id')

    # Фильтрация по году
    if year:
        movies = movies.filter(year=year, category="3").order_by('-id')

    context = {
        'movies': movies
    }

    return render(request, 'movies/serials.html', context)


def about(request):
    """Страница О сайте"""
    return render(request, 'movies/about.html')


def movie_trailer(request, pk):
    """Вывод трейлера"""
    movie = get_object_or_404(Movie, pk=pk)
    context = {'movie': movie}
    return render(request, 'movies/movie_detail.html', context)












# @login_required
# def index(request):
#     # tasks = Task.objects.find() - Найти по id
#     # tasks = Task.objects.order - Произвести сортировку
#     # tasks = Task.objects.order_by('-id')[:1] - Сортировка по id в обратном порядке, лишь по одной записи
#     tasks = Category.Movie.title.objects.order_by('-id')[:1]
#     return render(request, 'movies/movie_detail.html', {'title': 'Главная страница сайта', 'tasks': tasks})



