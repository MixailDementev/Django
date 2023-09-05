
from django.views.generic import TemplateView
from django.http import HttpResponse
import logging
from datetime import datetime

logger = logging.getLogger(__name__)



class MainPageView(TemplateView):
    template_name = 'site.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['name'] = 'Дементьев Михаил'
        contex['email'] = 'vanneste1207@gmail.com'
        contex['phone'] = '+79115715194'
        logger.info(f'посещение страницы: {datetime.now()}')
        return contex


class AboutView(TemplateView):
    template_name = 'author.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['name'] = 'Дементьев Михаил'
        contex['email'] = 'vanneste@rambler.ru'
        contex['phone'] = '+79115715194'
        logger.info(f'посещение страницы в: {datetime.now()}')
        return contex


def site(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Мой первый Django-сайт</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 20px;
            }
            
            h1 {
                color: #333;
            }
            
            p {
                color: #777;
            }
        </style>
    </head>
    <body>
        <h1>Добро пожаловать на мой первый Django-сайт!</h1>
    
        <h2>О сайте</h2>
        <p>Этот сайт разработан с использованием Django, мощного фреймворка для создания веб-приложений на языке Python. Здесь я могу создавать и отображать различные страницы и данные в удобном формате.</p>
    
        <h2>Обо мне</h2>
        <p>Привет, меня зовут Дементьев Михаил. Я являюсь инженером бортовой аппаратуры ракеты-носителя "Союз-2"</p>
    
        <footer>
            <p>Свяжитесь со мной: vanneste1207@gmail.com | +79115715194</p>
        </footer>
    </body>
    </html>
    """
    logger.info(f'посещение страницы site в: {datetime.now()}')
    return HttpResponse(html)


def author(request):
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Обо мне</title>
</head>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 20px;
            }
            
            h1 {
                color: #333;
            }
            
            p {
                color: #777;
            }
        </style>
<body>
    <header>
        <h1>Привет! Я, Дементьев Михаил.</h1>
    </header>

    <main>
        <section>
            <h2>Опыт работы</h2>
            <ul>
                <li>Место работы 1</li>
            </ul>
        </section>

        <section>
            <h2>Образование</h2>
            <ul>
                <li>Университет 1</li>
            </ul>
        </section>

        <section>
            <h2>Навыки</h2>
            <ul>
                <li>Навык 1</li>
                <li>Навык 2</li>
            </ul>
        </section>
    </main>

    <footer>
        <p>Свяжитесь со мной: vanneste@rambler.ru | +79115715194</p>
    </footer>
</body>
</html>
"""
    logger.info(f'посещение страницы author в: {datetime.now()}')
    return HttpResponse(html)