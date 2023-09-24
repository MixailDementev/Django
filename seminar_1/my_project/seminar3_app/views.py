from .models import Author, Post, Comment
from random import randint
from django.views.generic import TemplateView, DetailView


class HomeViews(TemplateView):
    template_name = 'seminar3_app/main_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

class AboutViews(TemplateView):
    template_name = 'seminar3_app/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обо мне'
        return context


class GameView(TemplateView):
    template_name = 'seminar3_app/game.html'

class HeadsGame(GameView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = [('TAILS', 'HEADS')[randint(0, 1)] for i in range(int(self.kwargs['count']))]
        context['results'] = results
        context['title'] = 'Игра в Орла и Решку'
        return context


class DiceGame(GameView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = [randint(1, 6) for i in range(int(self.kwargs['count']))]
        context['results'] = results
        context['title'] = 'Игра в Кости'
        return context


class AllPostViews(TemplateView):
    template_name = 'seminar3_app/posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = Author.objects.get(pk=self.kwargs['id_author'])
        posts = Post.objects.filter(author=author).all()
        context['posts'] = posts
        return context


class DetailPost(DetailView):
    model = Post
    template_name = 'seminar3_app/detail_posts.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views += 1
        obj.save()
        return obj








